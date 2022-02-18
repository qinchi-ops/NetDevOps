#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, Response
import json

node = Flask(__name__)
# 打开Debug
node.debug = True

# POST实现JSON RPC
@node.route('/eem', methods=['POST'])
def router_control():
    # res
    client_post_data = request.json
    if client_post_data:
        print(client_post_data)
        event = client_post_data.get('event')
        event_detail = client_post_data.get('event_detail')
        if event == 'ospf' and event_detail == 'DOWN':
            if client_post_data.get('interface') == 'GigabitEthernet2':
                return {'event':'ospf','cmd':"configure terminal ; interface GigabitEthernet3 ;  shutdown"}
        elif event == 'ospf' and event_detail == 'FULL':
            if client_post_data.get('interface') == 'GigabitEthernet2':
                return {'event':'ospf','cmd':"configure terminal ; interface GigabitEthernet3 ; no shutdown"}
        else:
            return {'error': f'no ospf status in json!:{event}'}

    else:
        return  {'error': 'no json data'}


if __name__ == "__main__":
    node.run(host='0.0.0.0', port=8080)
