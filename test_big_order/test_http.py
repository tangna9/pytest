#-*- coding:utf-8 -*-
__author__ = 'tangna'
import urllib
import urllib2
import json
import redis

def get_safe_stock_api_result():
    safe_stock_api = "http://10.3.255.229:9999/antifraud/api/orders"
    values = {"coupon_amount": 0, "cust_credit_used": 0, "cust_email": "testbl42@test.com", "cust_id": 55222213,
            "cust_type": 3, "device_id": '1212', "invoice_title": "", "mobile_phone_verify": "", "order_creation_date": "2015-11-29 16:56:42",
        "order_from_ip": "111.207.228.104", "order_id": 3308880005,"order_source": "dangdang","order_status": -100,"order_type": 97,
        "parent_id": 3308880004, "payment_method_type": 1,"payment_provider_id": -1,"permanent_id": "21212121212",
        "pick_up_id" : 16130, "pick_up_town_id": 1110105,"quarter_id": 1540302,"receiver_address": "朝阳区北三环东路8号静安中心2222号",
        "receiver_city_id": 14, "receiver_country_id": 9000, "receiver_mobile_tel": "11113331112", "receiver_name": "李四",
        "receiver_province_id": 154,"receiver_tel": "010-12345678","receiver_zip": "100028","shipping_fee": 0,"shipping_method_type": 11,
        "shop_id": 0, "total_bargin_price": 4699, "town_id":1540302,
        "order_items": [{"allot_quantity": 1, "bargin_price": 4699,"category_path": "58.80.03.00.00.00",
  "gift_product_id": 111,
  "is_presale": 0,
  "item_id": 1637695868001,
  "order_id": 3308880005,
  "order_quantity": 5,
  "product_id": 23753844,
  "product_name": "【当当自营】 三星 Galaxy Note3 N9008V 4G手机（白色）TD-LTE/TD-SCDMA/GSM (32G版）",
  "product_type": 88,
  "shipping_fee": 12
 }, {"allot_quantity": 1, "bargin_price": 2258,"category_path": "01.03.50.00.00.00",
  "gift_product_id": 111,
  "is_presale": 0,
  "item_id": 1637695868002,
  "order_id": 3308880005,
  "order_quantity": 1,
  "product_id": 22865986,
  "product_name": "测试测试测试测试品2",
  "product_type": 88,
  "shipping_fee": 12
 }
]}
    data = json.dumps(values)
    print data
    req = urllib2.Request(safe_stock_api, data)
    req.add_header("Content-type", "application/json")
    req.get_method = lambda: 'POST'
    response = urllib2.urlopen(req).read()
    print json.loads(response)

get_safe_stock_api_result()