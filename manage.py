import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
#Flask Script扩展提供向Flask插入外部脚本的功能，包括运行一个开发用的服务器，一个定制的Python shell，
from flask_migrate import Migrate, MigrateCommand 
#Flask-Migrate是用于处理SQLAlchemy 数据库迁移的扩展工具。当Model出现变更的时候，通过migrate去管理数据库变更。
#使用‘flask_migrate’必须借助‘flask_scripts’这个包的'MigrateCommand'中包含了所有和数据库相关的命令
#MigrateCommand类仅在需要通过flask脚本扩展公开数据库迁移命令时使用

app = create_app(os.getenv('FLASK_CONFIG') or 'default') #创建程序实例
manager = Manager(app) # #初始化扩展，Manager类追踪所有在命令行中调用的命令和处理过程的调用运行情况
migrate = Migrate(app, db)##初始化扩展，要迁移的两个参数是应用程序实例和flask sqlachemy数据库实例。

def make_shell_context():
    return dict(app=app, db=db, User=User,Role=Role)

@manager.command #@manage.command 作用是通过命令行可以访问这个方法
def test():
    """Run the unit test."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    #unittest.TextTestRunner(verbosity=2).run(suite)运行用例，
    # TextTestRunner类将用例执行的结果以text形式输出，
    # verbosity默认值为1，不限制完整结果，即单个用例成功输出’.’,失败输出’F’,错误输出’E’;
    # verbosity=2将输出完整的信息，verbosity=2是指测试结果的输出的详细程度，有0-6级，

#添加脚本命令
manager.add_command("shell", Shell(make_context=make_shell_context()))#自动导入对象
#自定义命令一，命令是shell，manager是Manager的实例，
# 调用add_command方法的效果是， 在终端使用shell命令后会调用Shell（make_context=make_shell_context）, 
#  Shell的作用就是调用make_shell_context函数得到对象字典， 然后再遍历字典导入对象。
manager.add_command('db', MigrateCommand) #数据库迁移,MigrateCommand
# 自定义命令二，命令是db

if __name__ == '__main__':
    manager.run() #调用manager.run()启动Manager实例接收命令行中的命令
