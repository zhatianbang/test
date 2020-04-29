# -*- coding: UTF-8 -*-
import unittest
from testutest import testlib
from parameterized import parameterized


# 创建一个测试类，继承unittest
class PramaTest(unittest.TestCase):

    @parameterized.expand([
        [1,1,2,"整数"],
        [1.1,1.33333333,2.43333333,"小数"],
        [1,5,12,"随便写"],
    ])
    def test_add(self,x,y,z,d=''):
        """"""
        print(d)
        self.assertEqual(testlib.add(x, y), z)

    def test_b(self):
        """不参数化的部分"""
        print(1111111111111111111111111111111111)

if __name__ == '__main__':
    unittest.main()
