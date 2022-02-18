# https://nornir.readthedocs.io/en/latest/tutorial/tasks.html
from nornir import InitNornir
# pip3 install nornir-utils
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result
# Nornir加载配置文件
nr = InitNornir(config_file="config.yaml")
# 通过过滤提取,希望应用Task(任务)的主机
nr = nr.filter(
    type="router",
    # site='beijing'
)


print('-'*50 + 'hello_world' + '-'*50)


# hello world
# Task, Result都是在控制类型而已, Python函数一般不控制输入和输出类型,但是可以通过下面的方式来控制类型
# 传入的参数task类型为Task
# 输出的结果类型为Result
def hello_world(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world!"
    )


result = nr.run(task=hello_world)  # 不定义name, 名字将会使用函数的名字 hello_world
# print_result漂亮的打印整个执行过程,打印显示而已!
print_result(result)

# 提取结果 .result与[0] 效果等价
# result['csr1'].result为此次任务执行的结果, result=f"{task.host.name} says hello world!"
print(f"本次任务CSR1的结果为: {result['csr1'].result}")
print(f"本次任务CSR2的结果为: {result['csr2'][0]}")


print('-'*50 + '传参数' + '-'*50)


# 添加参数
# Task, str, Result都是在控制类型而已, 传入的参数为text, 类型为str
def say(task: Task, text: str) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name} says {text}"  # 做了一个简单的字符串拼接
    )


result = nr.run(
    name="more parameters",  # 配置了任务名称
    task=say,
    text="welcome to qytang!"
)
# print_result漂亮的打印整个执行过程,打印显示而已!
print_result(result)

# 提取结果 .result与[0] 效果等价
# result['csr1'].result为此次任务执行的结果, result=f"{task.host.name} says {text}"
print(f"本次任务CSR1的结果为: {result['csr1'].result}")
print(f"本次任务CSR2的结果为: {result['csr2'][0]}")

print('-'*50 + '一组任务' + '-'*50)


# Grouping Tasks
def count(task: Task, number: int) -> Result:
    return Result(
        host=task.host,
        result=f"{[n for n in range(0, number)]}"
    )


def greet_and_count(task: Task, number: int) -> Result:
    task.run(
        name="Greeting is the polite thing to do",  # 任务一
        task=say,
        text="hi!",
    )

    task.run(
        name="Counting beans",  # 任务二
        task=count,
        number=number,
    )
    task.run(
        name="We should say bye too",  # 任务三
        task=say,
        text="bye!",
    )

    # let's inform if we counted even or odd times
    even_or_odds = "odd" if number % 2 == 1 else "even"  # 条件语句
    return Result(
        host=task.host,  # 应用到主机
        result=f"{task.host} counted {even_or_odds} times!",  # 返回最终结果
    )


result = nr.run(
    name="Counting to 5 while being very polite",
    task=greet_and_count,
    number=5,
)

print_result(result)
print(f"本次任务CSR1的结果为: {result['csr1'].result}")  # result=f"{task.host} counted {even_or_odds} times!"
print(f"本次任务CSR2的结果为: {result['csr2'][0]}")  # result=f"{task.host} counted {even_or_odds} times!"
