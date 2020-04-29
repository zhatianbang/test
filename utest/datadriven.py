# -*- coding: UTF-8 -*-
import inspect, sys, datetime
from common.Excel import Reader, Writer
from common import logger


reader = Reader()
writer = Writer()
alllist = []
runtype = 'WEB'
title =''


# 反射获取关键字
def geffunc(line, http):
    func = None
    try:
        func = getattr(http, line[0])
    except Exception as e:
        print(e)

    return func


# 反射获取参数
def getargs(func):
    if func:
        args = inspect.getfullargspec(func).__str__()
        args = args[args.find('args=') + 5:args.find(', varargs')]
        args = eval(args)
        args.remove('self')
        l = len(args)
        return l
    else:
        return 0


# 运行一条用例
def run(func, lenargs, line):
    # 如果没有这个函数，就不执行
    if func is None:
        return False

    if lenargs < 1:
        res = func()
        return res

    if lenargs < 2:
        res = res = func(line[1])
        return res

    if lenargs < 3:
        res = func(line[1], line[2])
        return res

    if lenargs < 4:
        res = func(line[1], line[2], line[3])
        return res

    print('error：目前只支持3个参数的关键字')


# 选择排序
def selectSort(height):
    # 外层循环代表轮次
    l = len(height)
    for i in range(0, l):
        # 内层循环，选择最大的
        # 以第一个人为基准，记录下标
        tmp = 0
        for j in range(1, l - i):
            if str(height[tmp]) < str(height[j]):
                # 记录最大值下标
                tmp = j

        # # 把最高的放到最后
        t = height[tmp]
        height[tmp] = height[l - i - 1]
        height[l - i - 1] = t

        # 交换
        # height[tmp], height[len(height) - i - 1] = height[len(height) - i - 1], height[tmp]

def mysort(lists):
    # 用来存下标
    l = []
    # 初始化一共有多少个元素
    list1 = []
    for i in range(len(lists)):
        l.append(i)
        list1.append(i)

    selectSort(l)
    # 处理将要执行的用例
    # 把将要被执行的元素，放到unittest执行的下标位置
    for i in range(len(l)):
        list1[l[i]] = lists[i]

    return list1



    """读取的结果是二维列表
    ['分组信息', '', '用例名', '关键字', '输入', '', '', '执行状态', '实际结果']
2020-03-01 20:30:16,055 - INFO - ['授权接口', '登录接口', '注册接口', '注销接口', '获取用户信息接口', '校验正常流程']
[['授权接口', '', '', '', '', ''], [3, '设置默认的doctor', 'adddoctor', '', '', ''], [4, '设置地址', 'setwsdl', 'http://112.74.191.10:8081/inter/SOAP?wsdl', '', ''])
    """

def getparams(casepath, resultpath):
    global reader, writer, alllist, runtype
    reader.open_excel(casepath) #   这里已经设置读取第一个sheet页了
    # 第一行
    reader.readline()

    # 第二行
    line = reader.readline()
    logger.exception(line)
    runtype = line[1]
    title = line[2]

    writer.copy_open(casepath, resultpath)
    sheetname = reader.get_sheets()     # 获取所有的sheetNames
    writer.set_sheet(sheetname[0])
    writer.write(1, 3, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))  # 对结果文件第二行第四列写入开始时间
    for sheet in sheetname:
        # 设置当前读写的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        # 默认写第7列
        writer.clo = 7
        list = [sheet, '', '', '', '', '']
        alllist.append(list)
        for i in range(reader.rows):
            list = [i]
            line = reader.readline()
            # 如果第一列或者第二列有内容，就是分组信息，不运行
            if len(line[0]) > 0 or len(line[1]) > 0:
                pass
            else:
                list += line[2:7]
                alllist.append(list)
    # 一般不会出现用例执行顺序问题，如果出现了，启用下面这行代码
    # alllist = mysort(alllist)

    # print(alllist)



# ll = []
# for i in range(100):
#     ll.append(1)
#
# mysort(ll)
