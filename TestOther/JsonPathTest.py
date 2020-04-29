# coding:utf8

import json,jsonpath
# from interface.inter import HTTP
#
# s = '{"status":"0","t":"1582351044832","set_cache_time":"","data":[{"location":"澳大利亚","titlecont":"IP地址查询","origip":"1.1.1.1","origipquery":"1.1.1.1","showlamp":"1","showLikeShare":1,"shareImage":1,"ExtendedLocation":"","OriginQuery":"1.1.1.1","tplt":"ip","resourceid":"6006","fetchkey":"1.1.1.1","appinfo":"","role_id":0,"disp_type":0}]}'
# # 先把字符串转为json
# s = json.loads(s)
# res = jsonpath.jsonpath(s,'status')[0]
# print(res)
#
# print(jsonpath.jsonpath(s,'$..location')[0])

import datetime,time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


s = "{'id': {'entityType': 'ASSET', 'id': '731a73f0-558b-11ea-a35c-b992a69e6084'}, 'createdTime': 1582386800815, 'additionalInfo': None, 'tenantId': {'entityType': 'TENANT', 'id': '25453870-a9bc-11e9-be21-f7760de09a70'}, 'customerId': {'entityType': 'CUSTOMER', 'id': '13814000-1dd2-11b2-8080-808080808080'}, 'name': '12313', 'type': '123123222'}"


s = json.loads(s)
print(s)
# res = jsonpath.jsonpath(s,'$...id')[0]
# print(res)