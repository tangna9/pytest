#-*- coding:utf-8 -*-
__author__ = 'tangna'

import xlrd
import urllib
import urllib2
import json
import redis
import time
from clean_data import *
from config import *
#from get_realtime_result import *

list_data = []
source = xlrd.open_workbook(data_file)
data = source.sheet_by_name(data_sheet)
product = source.sheet_by_name(product_sheet)

def format_request_data(new_data):
    #data = json.dumps(new_data)
    #请求数据转成python格式
    #new_data = json.loads(new_data)
    #如果device_id在excel中填写pc,将此字段值设为null
    if new_data['device_id'] == 'pc':
        new_data['device_id'] = None
    #将product_id，receiver_mobile_tel转为整型
    new_data['allot_quantity'] = None
    new_data['gift_product_id'] = None
    new_data['shipping_fee'] = None
    #new_data['receiver_mobile_tel'] = int(new_data['receiver_mobile_tel'])
    new_data['order_id'] = int(new_data['order_id'])
    new_data['receiver_zip'] = int(new_data['receiver_zip'])
    for i in new_data['order_items']:
        print "??????", i['product_id']
        i['product_id'] = int(i['product_id'])
        #i['bargin_price'] = int(i['bargin_price'])
    #再转回字符串，发送请求
    new_data = json.dumps(new_data)
    print "request_data:", new_data
    return new_data

#得到请求实时订单数据，将数据以POST请求发给实时订单api
def use_real_time_api(data_dict):
    real_time_api = "http://10.3.255.229:9999/antifraud/api/orders"
    values = format_request_data(data_dict)
    #return 1
    req = urllib2.Request(real_time_api, values)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'POST'
    response = urllib2.urlopen(req).read()
    #print "*"*20
    print json.loads(response)

#根据excel中的数据生成品的字典
def get_product(list_product, product_ready, order_id):
    #取得excel中的所有产品数据，生成多维列表
    for i in range(1, product.nrows):
        list_product.append(product.row_values(i))
    #将产品数据列表和title拼成字典
    for j in range(0, len(list_product)):
        product_dict = dict(zip(product_title, list_product[j]))
        #将品字典中的订单号修改为与订单一致
        product_dict['order_id'] = order_id
        product_ready.append(product_dict)
    return product_ready


#get data sheet values
for i in range(1, data.nrows):
    list_data.append(data.row_values(i))

#根据data页逐行生成数据并发post请求实时订单api，且发送请求之前清空相关数据库数据
mobile_list = []
for j in range(0, len(list_data)):
    #print j
    #print "*" * 20, list_data[j]
    data_dict = dict(zip(data_title, list_data[j]))
    data_dict['order_creation_date'] = time.strftime('%Y-%m-%d %H:%M:%S')
    #data_dict['order_creation_date'] = "2015-12-12 12:00:00"
    #将两个空列表传给生成品字典的方法
    data_dict['order_items'] = get_product(list_product=[], product_ready=[], order_id=data_dict['order_id'])

    #获得order_id，然后根据order_id删除各个数据库相关数据
    # order_id = int(data_dict['order_id'])
    # print 'order_id:', order_id
    # mobile = int(data_dict['receiver_mobile_tel'])
    # if mobile >= 10000000000 and mobile < 100000000000:
    #     clean_sms(mobile)
    # clean_data(order_id=order_id)
    #print "data_dict: ", data_dict
    use_real_time_api(data_dict)
    #trigger(order_id)
    #get_check_api_result(order_id)
    #read_redis_result(order_id=order_id)
    print "*-->"*10

