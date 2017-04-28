#-*- coding:utf-8 -*-
__author__ = 'tangna'
import urllib
import urllib2
import json
import httplib

url= "http://10.3.255.229:9999/antifraud/api/orders"
original_data = '''
{
"coupon_amount": 0,
"cust_credit_used": 0,
"cust_email":"testbl41@test.com",
"cust_id": 50232304,
"cust_type": 3,
"device_id": null,
"invoice_title": "",
"mobile_phone_verify": "",
"order_creation_date": "2015-11-29 16:56:42",
"order_from_ip": "111.207.228.104",
"order_id": 1107770001,
"order_source": "dangdang",
"order_status": -100,
"order_type": 0,
"parent_id": 1108880001,
"payment_method_type": 1,
"payment_provider_id": -1,
"permanent_id": "20121224110617804120244959611123594",
"pick_up_id" : 16130,
"pick_up_town_id": 1110105,
"quarter_id": 1110105,
"receiver_address": "北三环东路8号静安中心12层",
"receiver_city_id": 1,
"receiver_country_id": 9000,
"receiver_mobile_tel": "15210218561",u
"receiver_name": "tangna",
"receiver_province_id": 111,
"receiver_tel": "",
"receiver_zip": "100028",
"shipping_fee": 0,
"shipping_method_type": 11,
"shop_id": 0,
"total_bargin_price": 4699,
"town_id": null,
"order_items": [
 {
  "allot_quantity": null,
  "bargin_price": 4699,
  "category_path": "58.80.03.00.00.00",
  "gift_product_id": null,
  "is_presale": 0,
  "item_id": 1637695868001,
  "order_id": 1107770001,
  "order_quantity": 11,
  "product_id": 60562664,
  "product_name": "【当当自营】 三星 Galaxy Note3 N9008V 4G手机（白色）TD-LTE/TD-SCDMA/GSM (32G版）",
  "product_type": 88,
  "shipping_fee": null
 }
]
}
'''
conn = httplib.HTTPConnection(url)
headers = {"Content-Type":"application/json"}
data = json.dumps(original_data.replace('\n', ''))

request = urllib2.Request(url, data)
request.get_method = lambda: 'POST'
response = urllib2.urlopen(request).read()
print response