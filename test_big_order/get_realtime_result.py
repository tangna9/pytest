#-*- coding:utf-8 -*-
__author__ = 'tangna'
import xlrd
import urllib
import urllib2
import json
import redis
import time


def get_check_api_result(order_id):
    check_result_api = "http://10.3.255.229:9999/antifraud/api/orders/%s/result"
    req = urllib2.Request(check_result_api %order_id)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'GET'
    response = urllib2.urlopen(req).read()
    #print "*"*20
    print "result:", json.loads(response)

def trigger(order_id):
    print "******", order_id
    trigger_api = "http://10.3.255.229:9999/antifraud/api/orders/%s/trigger"
    req = urllib2.Request(trigger_api %order_id)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'GET'
    response = urllib2.urlopen(req).read()
    #print "*"*20
    print "trigger: ", json.loads(response)

def read_redis_result(order_id):
    r = redis.Redis(host='10.3.255.229', port=6379, db=2)
    middle_key = "LogBigOrder:oid:%s" %order_id
    final_key = "LogCheckOrderAPI:oid:%s" %order_id
    print middle_key, r.get(middle_key)
    print final_key, r.get(final_key)


#order_list = [6031118122,33011170122,33011170123,33011170124,33011170125]
#order_list = [7031118122,22011170122]
#order_list = [7031118124,22011170123]
#order_list = [70311181334, 22011171334]

# for i in order_list:
#     trigger(order_id=i)
#
# print "*--->" * 6
#
# for i in order_list:
#     get_check_api_result(order_id=i)
#     read_redis_result(order_id=i)
#     print "*--->" * 6

