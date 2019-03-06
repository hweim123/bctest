import HtmlTestRunner
import unittest


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print(22222)

    def test_run(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例

    def test_run2(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例

    def test_run3(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例

    def test_run1(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        # 测试用例


if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    test_suite.addTest(MyTest('test_run1'))  # 测试套件中添加测试用例
    # test_suite.addTest(unittest.makeSuite(MyTest))# 使用makeSuite方法添加所有的测试方法
    fp = open('F:\\res.html', 'wb')  # 打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
    # 生成执行用例的对象
    runner.run(test_suite)
    # 执行测试套件
