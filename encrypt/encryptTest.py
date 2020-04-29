# coding:utf8
import os

#
def decrypt(t,s):
    """
    使用decrypt.jar实现的加密解密算法
    :param t: 0表示加密，其他字符串表示解密
    :param s: 要加密和解密的字符串
    :return:
    """
    cmd ='java -jar decrypt.jar ' + str(t) +" " +str(s)
    result = os.popen(cmd).read()
    return result

# 执行cmd运行命令
res = os.popen('ipconfig').read()
# print(res)

# 在cmd中执行java命令运行jar
cmd ='java -jar decrypt.jar 0 123456'
res = os.popen(cmd).read()
print(res)

