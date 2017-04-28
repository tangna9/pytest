#-*- coding:utf-8 -*-
__author__ = 'tangna'

import redis
from pymongo import MongoClient
import MySQLdb

def exe_mysql(sql):
    try:
        conn = MySQLdb.connect(host="10.255.255.22", user="writeuser", passwd="ddbackend", db="RiskControl", port=3306)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" %(e.args[0], e.args[1])

def clean_sms(mobile):
    r = redis.Redis(host='10.3.255.229', port=6379, db=2)
    key = 'sms:mobi:%s' %mobile
    print key
    print r.hgetall(key)
    r.delete(key)

def clean_data(order_id):
    client = MongoClient("10.3.255.229", 27017)
    #print order_id
    db = client.antifraud
    order = db['order']
    # for i in order.find({"order_id": order_id}):
    #     print i
    order.remove({"order_id": order_id})
    print "mongo cleaned"

    r = redis.Redis(host='10.3.255.229', port=6379, db=2)
    results = r.keys('*%s' %order_id)
    if results:
        #print results
        for i in results:
            r.delete(i)
    print "redis order data cleaned"
    for i in ['log_check_order_api', 'log_big_order']:
        sql = "DELETE from %s where order_id in (%s)" %(i, order_id)
        exe_mysql(sql)
    #sql3 = "select * from log_big_order where order_id in (6031118122, 33011170122)"
    #print exe_mysql(sql3)
    print "mysql cleaned"

if __name__ == '__main__':
    #order_list = [6031118122,33011170122,33011170123,33011170124,33011170125]
    order_list = [1411541686]
    #order_list = [1116381001,1116381002,1116381003,1116381004,1116381005,1116381006,1116381007]
    mobile_list = [15811138435]
    for i in order_list:
        clean_data(order_id=i)

    for i in mobile_list:
        clean_sms(i)