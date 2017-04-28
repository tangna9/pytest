#-*- coding:utf-8 -*-
__author__ = 'tangna'

import redis
import urllib2
import urllib
import json

def get_bigorder_api_reslut(prod_id, cate_id, price):
    r = redis.Redis(host='10.3.255.229', port=6379, db=3)
    bizz_key = "big_order:cat:%s" %cate_id
    print "bizz_key", bizz_key
    bizz_value = r.hgetall(bizz_key)
    if bizz_value:
        print "bizz_value:%s %s and fee/bargin_price: %s" %(cate_id, bizz_value, float(bizz_value['fee'])/float(price))
        if bizz_value['op'] is '1':
            print "bizz_final_value: %s: %s:" %(cate_id, max(float(bizz_value['qty']), float(bizz_value['fee'])/float(price)))
        else:
            print "bizz_final_value: %s: %s:" %(cate_id, min(float(bizz_value['qty']), float(bizz_value['fee'])/float(price)))
    else:
        print "Bizz has no result!!!"
    #print "@@@"*5
    abc_key = "big_order:prod:%s" %prod_id
    abc_value = r.get(abc_key)
    if abc_value:
        print "abc_value: %s %s" %(prod_id, abc_value)
    else:
        print "abc_value: %s: ABC has no result!!!" %prod_id

    big_order_api = "http://10.3.255.229:8083/antifraud/api/bigorder_criteria"
    value = {"data":[{"product_id": prod_id, "category_path": cate_id, "bargin_price": price}]}
    data = json.dumps(value)
    print "大单审核请求数据: ", data
    req = urllib2.Request(big_order_api, data)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'POST'
    response = urllib2.urlopen(req).read()
    print "大单审核api返回结果：", json.loads(response)
    print "*--->" * 4
    return json.loads(response)

# list1 = (('60614730', '58.31.16.04.00.00', 18.9), ('60576835', '58.32.04.50.00.00', 12), ('23753844', '01.14.91.00.00.00', 4699), ('22865986', '01.03.50.00.00.00', 30.6),\
# ('60615444', '58.32.04.54.00.00', 12), ('60593071', '58.32.15.23.00.00', 3.8), ('60606504', '58.84.01.13.00.00', 99.9), ('60559841', '58.32.04.53.00.00', 8.8), \
# ('20947817', '01.21.03.05.00.00', 20.5), ('60606481', '58.32.04.53.00.00', 4.8),('60581151', '58.32.20.12.00.00', 29),('60608226', '58.84.01.11.00.00', 12.9),\
#              ('23567505', '01.24.03.00.00.00', 44.3), ('60588489', '58.32.18.02.00.00', 40),\
#              ('60576433','58.31.13.08.00.00',49),('60592494', '58.31.13.08.00.00', 12),('25034300','01.01.02.00.00.00',300),('60038780', '',39))
list1 = (('25005604','01.47.02.13.00.00',12),('25005607', '01.47.02.13.00.00',5),('25053240', '01.47.02.13.00.00',22.7),('25053516', '01.47.02.13.00.00',30.2),('25034300', '01.01.02.00.00.00',300),\
    ('60038780', '58.62.04.17.00.00',39),('25054006','01.01.05.00.00.00',69.69),('25053986','01.01.09.00.00.00',41))
list1= (('25005607', '58.31.05.12.01.00',5),)
for item in list1:
    print item
    get_bigorder_api_reslut(item[0], item[1], item[2])
