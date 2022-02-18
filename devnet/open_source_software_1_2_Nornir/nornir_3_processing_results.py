# https://nornir.readthedocs.io/en/latest/tutorial/task_results.html
import logging
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result

# instantiate the nr object
nr = InitNornir(config_file="config.yaml")

# let's filter it down to simplify the output
cmh = nr.filter(type="router")


def count(task: Task, number: int) -> Result:
    return Result(
        host=task.host,
        result=f"{[n for n in range(0, number)]}"
    )


def say(task: Task, text: str) -> Result:
    # 条件语句实战
    if task.host.name == "csr2":
        raise Exception("I can't say anything right now")
        # -------------------------------------强行抛出告警--------------------------------------
        # vvvv greet_and_count ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv ERROR
        # Subtask: Greeting is the polite thing to do (failed)
        #
        # ---- Greeting is the polite thing to do ** changed : False --------------------- ERROR
        # Traceback (most recent call last):
        #   File "/usr/local/lib/python3.8/site-packages/nornir/core/task.py", line 99, in start
        #     r = self.task(self, **self.params)
        #   File "/Open_Source_Software/open_source_software_1_2_Nornir/nornir_3_processing_results.py", line 22, in say
        #     raise Exception("I can't say anything right now")
        # Exception: I can't say anything right now
    return Result(
        host=task.host,
        result=f"{task.host.name} says {text}"
    )


def greet_and_count(task: Task, number: int):
    task.run(
        name="Greeting is the polite thing to do",
        severity_level=logging.DEBUG,  # 设置任务的日志级别
        task=say,
        text="hi!",
    )

    task.run(
        name="Counting beans",
        task=count,
        number=number,
    )
    task.run(
        name="We should say bye too",
        severity_level=logging.DEBUG,  # 设置任务的日志级别
        task=say,
        text="bye!",
    )

    # let's inform if we counted even or odd times
    even_or_odds = "odd" if number % 2 == 1 else "even"
    return Result(
        host=task.host,
        result=f"{task.host} counted {even_or_odds} times!",
    )


result = cmh.run(
    task=greet_and_count,
    number=5,
)

# 默认print_result打印级别为INFO以上事件, 设置成为logging.DEBUG的任务将不会被打印显示
print('-'*50 + 'print_result执行结果' + '-'*50)
print_result(result)
print('-'*50 + 'print_result执行结果' + '-'*50)

# As you probably noticed, not all the tasks were printed.
# This is due to the severity_level argument we passed.
# This let’s us flag tasks with any of the logging levels.
# Then print_result is able to follow logging rules to print the results.
# By default only tasks marked as INFO will be printed
# (this is also the default for the tasks if none is specified).

# 可以修改print_result打印的级别为logging.DEBUG, 这样就可以打印所有的事件!
print('-'*50 + 'print_result 打印的级别为logging.DEBUG 执行结果' + '-'*50)
print_result(result, severity_level=logging.DEBUG)
print('-'*50 + 'print_result 打印的级别为logging.DEBUG 执行结果' + '-'*50)

# 选择打印某一个步骤
print('-'*50 + 'print_result 打印某一个步骤 执行结果' + '-'*50)
print_result(result['csr1'][2])
print('-'*50 + 'print_result 打印某一个步骤 执行结果' + '-'*50)
# 你可以提取什么设备'csr1',第几次任务的结果
# .result 为 最终返回结果              :csr1 counted odd times!
# [0] 为 最终返回结果                  :csr1 counted odd times!
# [1] 为 第一个task say的返回结果       :csr1 says hi!
# [2] 为 task count的返回结果          :[0, 1, 2, 3, 4]
# [3] 为 第二个task say的返回结果       :csr1 says bye!
print(result['csr1'].result)
print(result['csr1'][0])
print(result['csr1'][1])
print(result['csr1'][2])
print(result['csr1'][3])

# 最终任务changed的结果
print("changed: ", result["csr1"].changed)

# 每一个小步骤changed的结果
print("changed: ", result["csr1"][1].changed)
