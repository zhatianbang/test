#coding:utf-8

import json
import requests
import random


# 1、建立一个session会话管理
session =requests.session()

# 2、发包  授权接口
res = session.post(url='http://112.74.191.10:8081/inter/HTTP/auth')  # 返回的是一个对象
print(res.text)  # 返回文本结果
print(res.content.decode('gbk'))  # 返回 内容,二进制的,可以指定编码格式解析
print(res.encoding)  # 返回 编码
# resJson = res.json()
# print(type(resJson))   # 返回的是json格式，即字典

jsonres = json.loads(res.text)

# 2.1、提取 token
token = jsonres['token']
# print(token)

# 3、注册
session.headers['token'] = token
name = 'Ronnie'+str(random.randint(1000,9999))
d = {'username':name,'pwd':'123456','nickname':'Ronnie的随机接口测试','describe':'接口测试描述'}

registerRes = session.post(url='http://testingedu.com.cn/inter/HTTP/register',data=d)
print(registerRes.text)

# 4、登录
d = {'username':name,'password':'123456'}
    # 接口接收的是标准的url格式参数，用data传递，如果是json，则使用 json=''传递
resLogin = session.post(url='http://112.74.191.10:8081/inter/HTTP/login',data=d)
print(resLogin.text)
# 4.1提取id给获取用户信息使用
id = (json.loads(resLogin.text))['userid']
# print(id)
# 5、 获取用户信息
d={'id':id}
getUserInfoRes = session.post(url='http://testingedu.com.cn/inter/HTTP/getUserInfo',data=d)
print(getUserInfoRes.text)

# 6、退出
logoutRes = session.post(url='http://112.74.191.10:8081/inter/HTTP/logout')
jsonLogout = json.loads(logoutRes.text)

# 7、断言
if jsonLogout['msg'] == '用户已退出登录' and jsonLogout['status'] == 200:
    print ('PASS')
else:
    print('FAIL')