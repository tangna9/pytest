#-*- coding:utf-8 -*-
__author__ = 'tangna'
import urllib
import urllib2
import json
import redis

#得到可销售库存
def get_stock_num(url, product):
    url = url %product
    print url
    stock_sum = 0
    response = urllib2.urlopen(url).read()
    print response
    data = json.loads(response)
    stock = data['product_warehouse_stock']
    for i in stock:
        stock_sum += i['sale_quantity']
        #print i['stock_quantity']

    print "productid: %s, 可销售库存stock_sum:%s" %(product, stock_sum)
    return stock_sum

def redis_conn():
    #r = redis.Redis(host='10.3.255.229', port=6379, db=3)
    r = redis.Redis(host='10.255.209.34', port=16379, db=4)
    return r
#得到redis中的日均*系数 和 单均*系数
def get_redis_stock_value(prod_id):
    prod_key = "stock:rule:prod:%s" %prod_id
    #print prod_key
    param_key = "stock:rule:param:%s" %prod_id
    r = redis_conn()
    prod = r.hgetall(prod_key)
    param = r.hgetall(param_key)
    if prod and param:
        print "redis_prod:", prod
        print "redis_param:", param
        standard = float(prod['avg_day'])*float(param['param_stock'])
        print "安全库存标准/avg_day*param_stock:", standard
        print "占库存标准prod/avg_order*param_order:", float(prod['avg_order'])*float(param['param_order'])

    elif prod and not param:
        print "redis_prod:", prod
        print "占库存没有参数 safe_stock_ratio_cate or prod没有数据在redis"
    elif param and not prod:
        print "redis_param:", param
        print "stock没有数据，日均单均没有数据"
    else:
        print "该品即没有日均单均，也没有对应系数"
    return standard
#请求安全库存api并查看返回结果
def get_safe_stock_api_result(prod_id):
    safe_stock_api = "http://10.3.255.229:8083/antifraud/api/safe_stock_check"
    values = {"data":[{"product_id":prod_id}]}
    data = json.dumps(values)
    #print data
    req = urllib2.Request(safe_stock_api, data)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'POST'
    response = urllib2.urlopen(req).read()
    print "安全库存api返回结果：", json.loads(response)
    return json.loads(response)


#url = "http://10.4.15.240/prodstock/queryprodstock.xhtml?product_id=%s&format=json"
url = "http://10.3.255.178:9099/prodstock/QueryProdStock.xhtml?product_id=%s&format=json"
#product_list = ('23753844','20947817','22817409','22865986','22501266','60585818','60563256','60595093','60617826','60606504')
product_list = ('60612065', '60614730', '23753844', '22865986', '60615444', '60576835', '60593071', '60606504','60559841',\
                '20947817', '60606481', '60581151','60608226','23567505','60588489','60576433','60592494','25034300')
product_list = (25005607,25053240,25053516,25034300,60038780,25053986)
count = 1
#
# for i in product_list:
#     print count
#     stock_num = get_stock_num(url, i)
#     standard = get_redis_stock_value(prod_id=i)
#     get_safe_stock_api_result(prod_id=i)
#     count += 1
#
# stock_prod_list = [25005604,25005607,25053240,25053516]
for i in ("61040561", ):
    url = "http://10.3.255.178:9099/prodstock/QueryProdStock.xhtml?product_id=%s&format=json"
    stock_num = get_stock_num(url, i)
    safe_stock_standard = get_redis_stock_value(i)
    print "*"*10, "自己乘天数吧，如果是货到付款，记得给安全库存标准乘以10哦"
    if stock_num > safe_stock_standard:
        print "不低于安全库存"
    else:
        print "低于安全库存"