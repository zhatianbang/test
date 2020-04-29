#coding:utf-8
from interface.inter import HTTP
from common.Excel import *
import inspect
from common.excelresult import Res
from common import config
from common.mail import Mail
import jsonpath

# def runcase(line):
#     if line[3]== 'post':
#         http.postJson(line[4],line[5],line[6])
#         return
#
#     if line[3] == 'assert':
#         http.assertequals(line[4],line[5])
#         return




# #**************************************
# func = getattr(http,'postJson')
# func("http://www.testingedu.com.cn/inter/HTTP/auth")
# args = inspect.getfullargspec(func).__str__()
# print(args)
#
# args = args[args.find("args=")+5:args.rfind(', varargs=None')]
# print(args)
#
# args = eval(args)
# args.remove('self')
# print(args)
# #**************************************


# #*********** 反射调用关键字 ***************************
def runcase(line):
    # 分组信息不用执行
    if len(line[0])>0 or len(line[1])> 0:
        return
    # 反射获取关键字函数
    func = getattr(http,line[3])
    # 获取参数列表
    args = inspect.getfullargspec(func).__str__()
    args = args[args.find('args=')+5:args.rfind(', varargs')]
    args = eval(args)
    args.remove('self')
    # 根据参数调用
    # print(len(args))
    if len(args)== 0:
        func()
        return

    if len(args) == 1:
        func(line[4])
        return

    if len(args) == 2:
        func(line[4],line[5])
        return

    if len(args) == 3:
        func(line[4],line[5],line[6])
        return

    print('warning:目前只支持三个关键字调用')


reader = Reader()
reader.open_excel('./lib/cases/百度ip.xls')
sheetname = reader.get_sheets()

writer = Writer()
writer.copy_open('./lib/cases/百度ip.xls', './lib/results/result-百度ip.xls')
http = HTTP(writer)
for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    # 设置写的sheet页，保持读和写是同一个sheet
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        writer.row = i
        line = reader.readline()
        runcase(line)


writer.save_close()

#     # 得到报告数据
# res = Res()
# r = res.get_res('./lib/results/result-百度ip.xls')
#
# # 读取配置文件
# config.get_config('./conf/conf.properties')
# logger.info(config.config)
# logger.info(config.config['mail'])
# # 修改邮件数据
# html = config.config['mailtxt']     # 读取报告模板
# html = html.replace('title',r['title']) # 替换模板中的数据
# html = html.replace('runtype',r['runtype'])
# html = html.replace('passrate',r['passrate'])
# html = html.replace('status',r['status'])
# html = html.replace('casecount',r['casecount'])
# html = html.replace('starttime',r['starttime'])
# html = html.replace('endtime',r['endtime'])
# if r['status'] == 'Fail':
#     html = html.replace('#00d800','red')
#
# mail = Mail()
# mail.send(html)