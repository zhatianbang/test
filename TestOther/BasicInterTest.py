# coding:utf-8

import requests, json,jsonpath
from urllib import parse
session = requests.session()

session.headers['content-type'] = 'application/json;charset=UTF-8'
session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
session.headers['sec-fetch-mode'] = 'cors'
session.headers['sec-fetch-site'] = 'same-origin'

url = 'https://test-cc.chintcloud.net/api/auth/login'
data = '{"username":"common-api@chint.com","password":"common-api"}'
d = json.loads(data)

res = session.post(url=url, json=d)
print(res.text)

resJson = json.loads(res.text)  # 返回结果转为json

res = jsonpath.jsonpath(resJson,'$.token')[0]   #提取token

session.headers['x-authorization']='Bearer ' +res  # 添加token
# 新增资产
d ='{"name":"12313","type":"123123222"}'
res = session.post(url='https://test-cc.chintcloud.net/api/asset',json=json.loads(d))
print(res.text)

resJson = json.loads(res.text)  # 返回结果转为json

id = jsonpath.jsonpath(resJson,'$.id.id')[0]   #提取id
print(id)

# 删除新增的资产
res = session.delete(url='https://test-cc.chintcloud.net/api/asset/'+ id)
print('删除的结果'+res.text)

# 查询资产
res = session.get(url='https://test-cc.chintcloud.net/api/tenant/assets?limit=100&textSearch=%E7%9B%B4%E8%BF%9E%E4%BA%A7%E5%93%81%E7%9B%B4%E8%BF%9E%E8%AE%BE%E5%A4%87')
print(res.text)
resJson = json.loads(res.text)  # 返回结果转为json
id = jsonpath.jsonpath(resJson,'$..id.id')   #提取id

# # 删除资产
if id:
    for i in range(len(id)):
        url='https://test-cc.chintcloud.net/api/asset/'+ id[i]
        print("待删除资产url+id:"+url)
        res = session.delete(url=url)
        print(res.text)


# 查询设备
# res = session.get(url='https://test-cc.chintcloud.net/api/tenant/devices?limit=100&textSearch=%E6%B5%8B%E8%AF%95%E8%AE%BE%E5%A4%87%E5%90%8D%E7%A7%B0')
res = session.get(url='https://test-cc.chintcloud.net/api/tenant/devices?limit%3D40%26textSearch%3D%E8%AE%BE%E5%A4%87')
print("无=号")
print(res.text)

resJson = json.loads(res.text)  # 返回结果转为json
id = jsonpath.jsonpath(resJson,'$..id.id')   #提取id

res = session.get(url='https://test-cc.chintcloud.net/api/tenant/devices?limit=40&textSearch%3D%E8%AE%BE%E5%A4%87')
print("有=号")
print(res.text)

# # # 删除设备
# if id:
#     for i in range(len(id)):
#
#         url='https://test-cc.chintcloud.net/api/device/'+ id[i]
#         print("待删除设备url+id:"+url)
#         res = session.delete(url=url)
#         print(res.text)




# #
# #
# #
# #
# # 编码
# import re
# zhmodel = re.compile(u'[\u4e00-\u9fa5]')
#
# contents = 'limit=40&textSearch=设备'
# match = zhmodel.search(contents)
# if match:
#     res = parse.quote(contents)
#     print('编码后')
#     print(res)
#     res = res.replace('%3D','=').replace('%26','&')
#     print(res)
#     if res == 'limit=40&textSearch=%E7%9B%B4%E8%BF%9E%E4%BA%A7%E5%93%81%E7%9B%B4%E8%BF%9E%E8%AE%BE%E5%A4%8726033':
#         print('编码后相等')
# else:
#     print(u'没有包含中文')
# #
# #
# #
