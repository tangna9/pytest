#-*- coding:utf-8 -*-
__author__ = 'tangna'

import redis
import json

def get_redis_check_result(order_id):
    check_order_key = "LogCheckOrderAPI:oid:%s" %order_id
    order_result_key = "LogBigOrder:oid:%s" %order_id
    #print check_order_key
    r = redis.Redis(host='10.3.255.229', port=6379, db=2)
    check_order_result = r.get(check_order_key)
    order_result = json.loads(r.get(order_result_key))
    print "check_order_result:", check_order_result
    print "*"*20
    print "order_result:", order_result
    print "*"*20
    print "order_result_tag_stock:", order_result['tag_stock']
    print "order_result_tag_bigorder:", order_result['tag_bigorder']
    print "order_result_chk_type:", order_result['chk_type']
    print "order_result_decision:", order_result['decision']
    print "order_result_sms_send_time:", order_result['sms_send_time']

order_list = ('23753844',)
for i in order_list:
    get_redis_check_result(order_id=i)