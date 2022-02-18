#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-
from netmiko import Netmiko
import time
import os
import paramiko
import threading
import datetime
import traceback
import re
current_path = os.getcwd()

# customize the following path

# the content of host list file should be:
# officename swname swip username password
# eg: DCname huawei 10.0.0.7 jack 123456
host_list_path = current_path + '/sw.txt'

# puts your commands to this file one by one line
command_list_path = current_path + '/command.txt'

# Don't add backslash at the end of path.
log_path = '/network/log'

# get current time
now = datetime.datetime.now()

# get thread lock
thread = threading.Lock()

# thread list
threads = []

# success hosts list
success_hosts = []

# failed hosts list
fail_hosts = []


def netmiko_show_cred(host, username, password, cmd, enable='Cisc0123', ssh=True):
    device_info = {
        'host': host,
        'username': username,
        'password': password,
        'device_type': 'cisco_ios' if ssh else 'cisco_ios_telnet',
        'secret': enable
    }
    try:
        net_connect = Netmiko(**device_info)
        return net_connect.send_command(cmd)


    except Exception as e:
        print(f'connection error ip: {host} error: {str(e)}')
        return

def run(swname, host, username, password, cmd,port=22):
    # run(swname, host, username, password, 22, day_dir, cmd)
        try:
            filename ="/%s:%i-%.2i-%.2i-%.2i:%.2i:%.2i.log" % (
            swname, now.year, now.month, now.day, now.hour, now.minute, now.second)
            with open(filename, "ab+") as fp:
                fp.write(netmiko_show_cred(host, username, password, cmd, enable='Cisc0123', ssh=True))
            print("Host %s was exported Successfully!" % host)
            success_hosts.append(host)
        except:
            fail_hosts.append(host)
            print("Can't connect to %s" % host)
            print("port=%s, username=%s, password=%s" % (port,username,password))
            traceback.print_exc()
            print("Thread exit!\n")
            # threading.current_thread.exit()
            return

def main():
 for line in open(host_list_path, 'r').read().splitlines():
  if line:
   try:
    officename, swname, host, username, password, cmd = re.split(',\s?', line)
   except:
    print("\nThe style of host list file is incorrect.\n")
    return
   office_dir = log_path + "/" + officename
   if not os.path.exists(office_dir):
    os.makedirs(office_dir)

   day_dir = office_dir + "/%i-%.2i-%i" % (now.year, now.month, now.day)
   if not os.path.exists(day_dir):
    os.mkdir(day_dir)
   bakconf_thread = run(swname, host, username, password,day_dir, cmd)
   bakconf_thread.start()
   threads.append(bakconf_thread)
 for t in threads:
  t.join()
 print("Finish!\nSucceeded hosts: %s\nFailed hosts: %s" % (success_hosts, fail_hosts))

if __name__ == '__main__':
    print(netmiko_show_cred('192.168.19.201', 'cisco', 'cisco123', 'undebug all'))
    # raw_result = netmiko_show_cred('192.168.19.201', 'cisco', 'cisco123', 'show run')
