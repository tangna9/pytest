#encoding:utf8
__author__ = 'tangna'

import urllib2
import json
import xlrd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def read_data():
    content = xlrd.open_workbook('D:\\workplace\\test_big_order\\test_data.xlsx')
    table = content.sheet_by_index(0)
    column = 1
    for i in xrange(0, table.nrows):
        order = table.cell(i, column).value
        jsoned_order = json.loads(order)
    return jsoned_order

def post_request(choice):
    if choice == "notify":
        request_url = "http://10.3.255.229:8081/antifraud/api/notify"
        data = '''{
                "event_id": 201,
                "content": {
                "cust_id": 13587714,
                "timestamp": 1462636800
                        }
                }'''
    elif choice == "order":
        request_url = "http://10.3.255.229:8081/antifraud/api/orders"
        data = json.dumps(read_data())
        print data
    req = urllib2.Request(request_url, data)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: "POST"
    response = urllib2.urlopen(req).read()
    print json.loads(response)

def add_order_id(data, step):

post_request("order")
#read_data()