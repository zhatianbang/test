import unittest,datetime,time
from parameterized import parameterized
from web.Web import Browser
from app.App import APP
from interface.inter import HTTP,SOAP
from utest import datadriven


class TestWeb(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = None
        if datadriven.runtype == 'WEB':
            cls.obj = Browser(datadriven.writer)

        if datadriven.runtype == 'APP':
            cls.obj = APP(datadriven.writer)

        if datadriven.runtype == 'HTTP':
            cls.obj = HTTP(datadriven.writer)

        if datadriven.runtype == 'SOAP':
            cls.obj = SOAP(datadriven.writer)

    # 关键字执行
    @parameterized.expand(datadriven.alllist)
    def test_all(self,index, name, key, param1, param2, param3):
        """
        :param index: datadriven.writer中第一个元素，设置index也是为了解决读和写的结果保持在同一行
        :param name: excel中的用例名
        :param key: excel中的关键字
        :param param1:excel中的第1个参数
        :param param2:excel中的第2个参数
        :param param3:excel中的第3个参数
        :return:
        """
        print(name)
        # 标识是否运行
        flg = False
        try:
            index = int(index)  # 如果第一个元素是数字，表示是需要执行的用例
            # 设置当前执行写入的行数
            datadriven.writer.row = index   # 让读和写保持在同一行
            # 如果不是sheet就运行
            flg = True
        except:
            # 如果是sheet，就切换写入的sheet页面，让读和写保持在同一sheet页
            datadriven.writer.set_sheet(index)

        # 如果需要运行用例
        if flg:
            line = [key, param1, param2, param3]
            print(line)
            # 反射获取要执行的关键字，如获取post，get，assert，addheader等
            func = datadriven.geffunc(line, self.obj)
            # print(func)
            # 获取参数的数目
            lenargs = datadriven.getargs(func)
            # 反射执行
            res = datadriven.run(func, lenargs, line)
            # 如果要断言有效，必须关键字里面添加：如果执行失败，就返回False
            if res is False:
                self.fail('关键字执行失败')


