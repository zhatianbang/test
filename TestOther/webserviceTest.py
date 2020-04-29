# coding:utf8
from suds.client import Client
import json,jsonpath
# 1、授权接口
url = 'http://112.74.191.10:8081/inter/SOAP?wsdl'
client = Client(url=url)
res = client.service.auth() # 通过webservice服务的client对象去调用服务
print(res)

res = json.loads(res)
token = jsonpath.jsonpath(res,'$.token')[0]
print(token)

#
# 2、登录接口
client = Client(url='http://112.74.191.10:8081/inter/SOAP?wsdl',headers={'token':token})
res = client.service.login('Ronnie8677','123456')
print(res)

# 3、退出
res = client.service.logout()
print(res)



# 反射测试
client = Client(url='http://112.74.191.10:8081/inter/SOAP?wsdl')
res = client.service.__getattr__('auth')()
print(res)

param = 'Ronnie8677、123456'
parmlist =param.split('、')
print(parmlist)
res = client.service.__getattr__('login')(*parmlist)
print(res)
print("***********************")

# 部分webservices接口需要指定命名空间
from suds.xsd.doctor import  Import,ImportDoctor
imp  = Import('http://www.w3.org/2001/XMLSchema',location='http://www.w3.org/2001/XMLSchema.xsd')
# 指定命名空间
imp.filter.add('http://WebXml.com.cn/')
doctor = ImportDoctor(imp)
client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl',doctor=doctor)
res = client.service.__getattr__('getSupportCity')('湖南')
print(res)