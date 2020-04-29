#coding:utf-8
from interface.inter import HTTP
import random

http = HTTP()
http.postJson('http://112.74.191.10:8081/inter/HTTP/auth')
http.assertequals('status','200')
http.savaJson('token','t')
http.addheader('token','{t}')
# 3、登录  # # d={'username':'Ronnie2658','password':'123456'}   # 这种也可以
http.postJson('http://112.74.191.10:8081/inter/HTTP/login',d= 'username=Ronnie2658&password=123456')
http.assertequals('status',200)
# 4、获取用户信息
http.savaJson('userid','id')     # savaJson(self,key,p)中self.param[p] = self.jsonres[key]，即保存的参数id2为键，userid为上一个请求返回的json的键
# print("保存的参数",http.param)  # 注意这时候param中保存了多个参数了，这样，如果下个请求需要多个参数，直接使用即可

# 这里d='id={id2}',其中id2必须与上一步http.savaJson('userid','id2')的id2保持一致，因为 postJson中调用__get_param(self, s)方法，它是遍历已经保存的参数，并将传入的字符串里面，满足{key}所有字符串用key对应的值来替换,如无，则不替换
http.postJson(url='http://testingedu.com.cn/inter/HTTP/getUserInfo',d='id={id}')
http.assertequals('status',200)


# 5、退出登陆
http.postJson('http://112.74.191.10:8081/inter/HTTP/logout')
# print(http.jsonres)
http.assertequals('status',200)