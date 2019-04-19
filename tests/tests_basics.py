import unittest
from flask import current_app
from app import create_app, db

class BasicTestCase(unittest.TestCase):
#定义测试类，父类为unittest.TestCase。
#可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
#可继承unittest.TestCase的各种断言方法。
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    #定义setUp()方法用于测试用例执行前的初始化工作。
    #注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    #注意，输入的值为字符型的需要转为int型

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    #定义tearDown()方法用于测试用例执行之后的善后工作。
    #注意，方法的入参为self

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    #定义测试用例，以“test_”开头命名的方法
    #注意，方法的入参为self
    #可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    #可定义多个测试用例
    #最重要的就是该部分
