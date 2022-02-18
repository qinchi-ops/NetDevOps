import requests
import urllib3
from bs4 import BeautifulSoup

devices_info = [
    {'name':'PythonAddDevice1',
                      'ip_address':'4.3.2.1',
                      'ro_community':'qytangro',
                      'rw_community':'qytangrw',
                      'username':'pythonsshusername',
                      'password':'pythonsshpassword',
                      'enable_password':'CIsco0123',
                      'device_type':'ASA'},
                     {'name': 'PythonAddDevice2',
                      'ip_address': '4.3.2.2',
                      'ro_community': 'qytangro',
                      'rw_community': 'qytangrw',
                      'username': 'pythonsshusername',
                      'password': 'pythonsshpassword',
                      'enable_password': 'CIsco0123',
                      'device_type': 'ASA'}

    ]

def config_device_info(username, password):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = 'http://djg.mingjiao.org/accounts/login/'
    # url = 'http://192.168.19.3/accounts/login/'
    username = str(username)
    password = str(password)

    # 建立并保持会话
    client = requests.session()
    # 获取登录页面的内容
    qytang_home = client.get(url)
    # qytang_home = client.get(url, verify=False)
    rp = requests.get(url)
    print(qytang_home)
    qytang_soup = BeautifulSoup(qytang_home.text, 'lxml')
    # 找到csrf令牌的值
    csrftoken = qytang_soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
    # 构建用户名, 密码和csrf值的POST数据
    login_data = {'username': username, 'password': password, "csrfmiddlewaretoken": csrftoken}

    # POST提交数据到登录页面
    client.post(url, data=login_data, verify=False)

    r = client.get('http://djg.mingjiao.org/add_devices')
    device_soup = BeautifulSoup(r.text, 'lxml')
    print(device_soup)
    # 找到csrf令牌的值
    csrftoken = device_soup.find('input', attrs={'type': "hidden", "name": "csrfmiddlewaretoken"}).get('value')
    # 构建用户名, 密码和csrf值的POST数据

    try:
        for device in devices_info:
            device.update({"csrfmiddlewaretoken": csrftoken})
            r = client.post('http://djg.mingjiao.org/add_devices', data=device, verify=False)
            BeautifulSoup(r.text, 'lxml')
            print('add device {0} successfully!'.format(device.get('name')))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    config_device_info('user1', 'cisco123')
