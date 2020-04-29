# coding:utf8
import requests

session = requests.session()
requests.packages.urllib3.disable_warnings()
session.headers['content-type'] = 'application/x-www-form-urlencoded'
session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
session.headers['x-zse-83'] = '3_2.0'

res = session.post('https://www.zhihu.com/udid')
print(res.text)

res = session.get("https://www.zhihu.com/api/v3/oauth?lang=cn")
print(res.text)

url ='https://www.zhihu.com/api/v3/oauth/sign_in'
data ='aRRGEvcmFqSfxhYq8LF0gHcBEgNVeCSMAhYqk4U0g_LxcTYhKUVBErS0cT2tEgNmqgSMxU9qkLk9-qNZsUO1iugZoGVVxhYq8Ln9k4U0gXLxcTYhBupGeheVkCN_evx9BLfBFUCG-qVGNCNMMTYhXg9hgqxOcvSMccxGcrU0g6SYXqYhqbO8ArU0g_LxgXx1h9pMUgHqkLPLQHYymiS1Hue1H9Lxg_NMwGoM2JXMST2tJvS8XXVMQ69qkLfxc0FqMMYqe7u92LkYJwNm8CSMcrU0g8NxSLOB0BOqgq9ygBtpQ7tqY028e0uBc72fe0YyhUYBc7H82HtYb0x9BLfBkvwGUbOYDq3q8Ln8gcgZcUS_iD3ZpvS8Xg9hgqxOcvSMMTYho49qS_2xoL2087Yqr6S0gRo9U9oMzcO1erU0g_xO-GoMBwxMXg9hguoLevwGXwNM3rU0gRtxguFqm0YBrAHqgg2f2Txy0qtq6A98S8Yfo8OBhq28Xg9hHgOGebOBtrS8'
res = session.post(url=url,data=data,verify=False)
print(res.text)

