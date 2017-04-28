#-*- coding:utf-8 -*-
__author__ = 'tangna'

import xlrd
import urllib
import urllib2
import json
import redis
import time

list_data = []
data_title = ['coupon_amount', 'cust_credit_used', 'cust_email', 'cust_id', 'cust_type', 'device_id', 'invoice_title', \
         'mobile_phone_verify', 'order_creation_date', 'order_from_ip', 'order_id', 'order_source', 'order_status', \
         'order_type', 'parent_id', 'payment_method_type', 'payment_provider_id', 'permanent_id', 'pick_up_id', 'pick_up_town_id', \
         'quarter_id', 'receiver_address', 'receiver_city_id', 'receiver_country_id', 'receiver_mobile_tel', 'receiver_name', \
         'receiver_province_id', 'receiver_tel', 'receiver_zip', 'shipping_fee', 'shipping_method_type', 'shop_id', 'total_bargin_price', 'town_id', 'order_items']
product_title = ['allot_quantity', 'bargin_price', 'category_path', 'gift_product_id', 'is_presale', \
                 'item_id', 'order_id', 'order_quantity', 'product_id', 'product_name', 'product_type', 'shipping_fee']
source = xlrd.open_workbook('D://test.xlsx')
num_sheets = source.sheets()
data = source.sheet_by_name('data')
product = source.sheet_by_name('product')

#得到请求实时订单数据，将数据以POST请求发给实时订单api
def use_real_time_api(request_data):
    safe_stock_api = "http://10.3.255.229:9999/antifraud/api/orders"
    values = request_data
    data = json.dumps(values)
    print "request_data:", data
    #请求数据转成python格式，将product_id，bargin_price字段转成整形
    new_data = json.loads(data)
    for i in new_data['order_items']:
        i['product_id'] = int(i['product_id'])
        i['bargin_price'] = int(i['bargin_price'])
    #再转回字符串，发送请求
    new_data = json.dumps(new_data)
    #return 1
    req = urllib2.Request(safe_stock_api, new_data)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'POST'
    response = urllib2.urlopen(req).read()
    #print "*"*20
    print json.loads(response)

#根据excel中的数据生成品的字典
def get_product(list_product, product_ready, order_id):

    for sheet in num_sheets:
        print sheet
        #取得excel中的所有产品数据，生成多维列表
        for i in xrange(1, product.nrows):
            list_product.append(product.row_values(i))
        #将产品数据列表和title拼成字典
        for j in xrange(0, len(list_product)):
            product_dict = dict(zip(product_title, list_product[j]))
            #将品字典中的订单号修改为与订单一致
            product_dict['order_id'] = order_id
            product_ready.append(product_dict)
        return product_ready


#get data sheet values
for i in xrange(1, data.nrows):
    list_data.append(data.row_values(i))

#produce data dict
for j in xrange(0, len(list_data)):
    #print j
    #print "*" * 20, list_data[j]
    data_dict = dict(zip(data_title, list_data[j]))
    data_dict['order_creation_date'] = time.strftime('%Y-%m-%d %H:%M:%S')
    #将两个空列表传给生成品字典的方法
    data_dict['order_items'] = get_product(list_product=[], product_ready=[], order_id=data_dict['order_id'])
    #print "data_dict: ", data_dict
    use_real_time_api(data_dict)


