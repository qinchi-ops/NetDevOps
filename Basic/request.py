
#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import requests

url = 'https://zbx.odcservice.com'
fout = open('zbxtest.txt', 'w')
for i in range(600):
    r=requests.get(url)
    fout.write(str(i+1)+' ： OK with status_code: '+str(r.text)+'\n')
    print(str(i+1)+' ： OK with status_code: '+str(r.text)+'\n')
    #print(str(i+1))
fout.close()