#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 20:00
# @Author  : Tang Na
# @Site    : 
# @File    : redis_realtime_search.py
# @Software: PyCharm Community Edition
import redis

#ad_id="20170818135612521463987"
#ad_id="20170905103504900887230"
ad_id="20170905103302128777229"
plan_id="287"
account_id = "1016"
app_id="f752cbbcedf842b68fc060cf899b10fa"

local_host="10.0.8.199"
far_host="172.20.1.161"
realtime_port=6383
offline_port=6382
real_db3=3
real_db10=10
offline_db4=4

local_r3= redis.Redis(host=local_host, port=realtime_port, db=real_db3)
far_r3= redis.Redis(host=far_host, port=realtime_port, db=real_db3)
local_r4= redis.Redis(host=local_host, port=offline_port, db=offline_db4)
far_r4= redis.Redis(host=far_host, port=offline_port, db=offline_db4)
local_r10= redis.Redis(host=local_host, port=realtime_port, db=real_db10)
far_r10= redis.Redis(host=far_host, port=realtime_port, db=real_db10)
#define key-realtime
key_advertiser_cost="AD_BDP_SENSEAR_ADVERTISER_COST_DATA:%s"%account_id
key_plan_cost="AD_BDP_SENSEAR_ADPLAN_COST_DATA:%s"%plan_id
key_ad_cost="AD_BDP_SENSEAR_AD_COST_DATA:%s"%ad_id
key_ad_statistics="AD_BDP_SENSEAR_AD_STATISTICS_DATA:%s"%ad_id
key_auth="AD_BDP_SENSEAR_AUTH_COUNT:%s"%app_id
key_auth_in="AD_BDP_SENSEAR_INTERNAL_AUTH_COUNT:%s"%app_id
key_ad_show="SARA_KEY_USER_AD_SHOW:%s*%s" %(app_id, ad_id)
key_user_info= "AD_BDP_SENSEAR_USER_INFO:%s*" %(app_id)
#define key-offline

local_advertiser_cost =local_r3.hgetall(key_advertiser_cost)
print  "local:"+key_advertiser_cost+":", local_advertiser_cost
far_advertiser_cost =far_r3.hgetall(key_advertiser_cost)
print  "far:"+key_advertiser_cost+":", far_advertiser_cost

print "#"*10

local_plan_cost =local_r3.hgetall(key_plan_cost)
print "local:"+key_plan_cost+":", local_plan_cost
far_plan_cost =far_r3.hgetall(key_plan_cost)
print "far:"+key_plan_cost+":", far_plan_cost

print "#"*10

#local_ad_cost = local_r3.hgetall(key_ad_cost)
#print  "local:"+key_ad_cost+":", local_ad_cost
#far_ad_cost = far_r3.hgetall(key_ad_cost)
#print  "far:"+key_ad_cost+":", far_ad_cost

print "#"*10
local_ad_statistics = local_r3.hgetall(key_ad_statistics)
print  "local:"+key_ad_statistics+":", local_ad_statistics
far_ad_statistics = far_r3.hgetall(key_ad_statistics)
print  "far:"+key_ad_statistics+":", far_ad_statistics

print "#"*10

local_auth = local_r3.hgetall(key_auth)
print  "local:"+key_auth+":",local_auth
far_auth = far_r3.hgetall(key_auth)
print  "far:"+key_auth+":",far_auth

#print "#"*10
#local_auth_in = local_r3.hgetall(key_auth_in)
#print  "local:"+key_auth_in+":",local_auth_in
#far_auth_in = far_r3.hgetall(key_auth_in)
#print  "far:"+key_auth_in+":",far_auth_in

print "#"*10
local_show_key=local_r3.keys(key_ad_show)
far_show_key=far_r3.keys(key_ad_show)

if local_show_key:
    for i in local_show_key:    
        print "local:"+i+":", local_r3.hgetall(i)
else:
    print local_show_key, "local empty!!!"

if far_show_key:
    for i in far_show_key:    
        print "far:"+i+":", far_r3.hgetall(i)
else:
    print far_show_key, "far empty!!!"

print "#"*10
local_info_keys=local_r3.keys(key_user_info)
local_user_info_num = len(local_info_keys)
print  "local:"+key_user_info+":",local_user_info_num
far_info_keys=far_r3.keys(key_user_info)
far_user_info_num = len(far_info_keys)
print  "far:"+key_user_info+":",far_user_info_num


print "#"*10

