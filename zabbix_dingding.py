#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import requests
import json
import sys
import os
import re
cdsb_group=["15196638082","18116564276"]
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "https://oapi.dingtalk.com/robot/send?access_token=a2b06dff06ce42eddb119afb155813fc2f4f642b31914fdd50d1e9eab4a9ecd9"

def get_hostgroup(hostgroup):
    hostgroup=str(hostgroup)
    if re.match('cdsb',hostgroup):
        number=cdsb_group
        return number
    else:
	print 'No match group'
	sys.exit()
def msg(text,hostgroup):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles":hostgroup,
            "isAtAll": False
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content
     
if __name__ == '__main__':
    f = open("/tmp/zabbix_dingding.log", 'a')
    group=sys.argv[1]
    hostgroup=get_hostgroup(group)
    text =sys.argv[2]
    msg(text,hostgroup)
