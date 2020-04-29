import unittest
from testutest import testadd


class MyTest(unittest.TestCase):
    """
    #继承unitest的TestCase类
    多个类时，鼠标在某个类的所在位置范围类，右键执行，则只执行该类
    """
    def setUp(self) :
        '''实例函数的setUp,每个测试方法执行前执行一次'''

        print("这是setUp的初始化")

    def test_01(self):
        """这是一个测试类，必须以test命名开头"""
        # print("这是一个测试方法1")
        res = testadd.add(2, 2)
        self.assertEquals(res, 3)

    def test_02(self):
        """这是一个测试类，必须以test命名开头"""
        # print("这也是一个测试方法2")

        res = testadd.add(1, 3)
        self.assertEquals(res, 4)




    @classmethod
    def setUpClass(cls) :
        '''类函数的setUp,只会在最开始执行'''
        print('类函数的setUp,只会在最开始执行一次')

    @classmethod
    def tearDownClass(cls) :
        '''类函数的setUp,只会在最开始执行'''
        print('类函数的setUp,只会在最后执行一次')

    def tearDown(self):
        '''每个测试方法执行后执行一次'''
        print("这是tearDown")

if __name__ == '__main__':
    """
    好处之一：在任何位置右键运行都能运行所有的测试方法
    坏处：没有默认报告"""
    unittest.main()