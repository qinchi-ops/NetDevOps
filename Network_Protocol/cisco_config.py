#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import netmiko
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


def netmiko_config_cred(host, username, password, cmds_list, enable='Cisc0123', ssh=True, verbose=False):
    device_info = {
                    'host': host,
                    'username': username,
                    'password': password,
                    'device_type': 'cisco_ios' if ssh else 'cisco_ios_telnet',
                    'secret': enable
    }
    try:
        net_connect = Netmiko(**device_info)
        if verbose:
            output = net_connect.send_config_set(cmds_list)
            return output
        else:
            net_connect.send_config_set(cmds_list)

    except Exception as e:
        print(f'connection error ip: {host} error: {str(e)}')
        return

class Bakconf(threading.Thread):
 def __init__(self, swname, host, username, password, port, day_dir, screen_command):
  threading.Thread.__init__(self)
  self.swname = swname
  self.host = host
  self.username = username
  self.password = password
  self.port = port
  self.log_dir = day_dir
  self.screen_command = screen_command

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
 def run(self):
  try:
   paramiko.util.log_to_file('ssh.log')
   # ssh_key = paramiko.RSAKey.from_private_key_file("/home/private/id_rsa")
   ssh_client = paramiko.SSHClient()
   ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   # thread.acquire()
   print("Connecting to server %s" % self.host)
   ssh_client.connect(self.host, self.port, self.username, self.password, allow_agent=False, look_for_keys=False,
                      timeout=10)
   # ssh_client.connect(self.host, self.port, self.username, pkey = ssh_key, allow_agent = False, look_for_keys = False, timeout=10)
   print("Successfully connected to server %s." % self.host)
   # thread.release()
   chan = ssh_client.invoke_shell()
   time.sleep(2)
   if chan.send_ready():
    chan.send(self.screen_command + '\n')
   else:
    raise("Channel not ready!")

   filename = self.log_dir + "/%s:%i-%.2i-%.2i-%.2i:%.2i:%.2i.log" % (self.swname, now.year, now.month, now.day, now.hour, now.minute, now.second)
   with open(filename,"ab+") as fp:
    for command in open(command_list_path, 'r').readlines():
     chan.send(command +'\n')
     print("%s is running. Sleep for 30 seconds!" % self.host)
     time.sleep(15)
     fp.write(chan.recv(999999))
     print("Host %s was exported Successfully!" % self.host)
   chan.send('quit\n')
   ssh_client.close()
   success_hosts.append(self.host)
  except:
   fail_hosts.append(self.host)
   print("Can't connect to %s" % self.host)
   print("port=%s, username=%s, password=%s" % (self.port, self.username, self.password))
   traceback.print_exc()
   print("Thread exit!\n")
   # threading.current_thread.exit()
   return

def main():
 for line in open(host_list_path, 'r').read().splitlines():
  if line:
   try:
    officename, swname, swip, username, password, screen_command = re.split(',\s?', line)
   except:
    print("\nThe style of host list file is incorrect.\n")
    return
   office_dir = log_path + "/" + officename
   if not os.path.exists(office_dir):
    os.makedirs(office_dir)

   day_dir = office_dir + "/%i-%.2i-%i" % (now.year, now.month, now.day)
   if not os.path.exists(day_dir):
    os.mkdir(day_dir)
   bakconf_thread = Bakconf(swname, swip, username, password, 22, day_dir, screen_command)
   bakconf_thread.start()
   threads.append(bakconf_thread)
 for t in threads:
  t.join()
 print("Finish!\nSucceeded hosts: %s\nFailed hosts: %s" % (success_hosts, fail_hosts))

if __name__ == '__main__':
    raw_result = netmiko_show_cred('192.168.19.201', 'cisco', 'cisco123', 'show run')
    # print(type(raw_result))
    print(raw_result)
    #
    # config_commands = ['router ospf 1',
    #                    'router-id 1.1.1.1',
    #                    'network 1.1.1.1 0.0.0.0 a 0']
    #
    # print(netmiko_config_cred('192.168.19.201', 'cisco', 'cisco123', config_commands, verbose=True))

