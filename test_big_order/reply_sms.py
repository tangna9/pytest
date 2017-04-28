#-*- coding:utf-8 -*-
__author__ = 'tangna'
import urllib
import urllib2
import json
import redis

def reply_sms():
    safe_stock_api = "http://10.3.255.229:8081/antifraud/api/sms/recv"
    values = {
             "mobile": 14771502231,
             "content": "y-61"
            }
    data = json.dumps(values)
    #print data
    req = urllib2.Request(safe_stock_api, data)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'POST'
    response = urllib2.urlopen(req).read()
    print json.loads(response)
    return json.loads(response)

def send_black_request():
    blank_first_api = "http://10.3.255.229:8083/antifraud/api/blacklist_1st"
    values = {
                    "cust_id": 3587714,
                    "cust_mobile_tel": "13661502230",
                    "receiver_mobile_tel": "null",
                    "receiver_tel": "01078782223",
                    "device_id": "113be00b08gg8e111146863",
                    "mobile_imei": "130025000000002",
                    "mobile_imsi": "460025000000002",
                    "mobile_mac": "68:1f:28:09:80:17"
    }
    data = json.dumps(values)
    #print data
    req = urllib2.Request(blank_first_api, data)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'POST'
    response = urllib2.urlopen(req).read()
    print json.loads(response)
    return json.loads(response)
reply_sms()
#send_black_request()