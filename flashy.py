import os 
from app import create_app, db
from app.models import User,Role
from flask_migrate import Migrate
from manage import manager 
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#os.getenv()获取一个环境变量，如果没有返回None
# os.getenv()来获取环境变量中的flask_config.然后执行
migrate = Migrate(app, db) #使用Migrate(app,db)来绑定app和数据库

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,Role=Role)
#make_shell_context()方法构建了数据库实例和models

@app.cli.command()
def test():
    """Run the unit test."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)
    #unittest.TextTestRunner(verbosity=2).run(suite)运行用例，
    # TextTestRunner类将用例执行的结果以text形式输出，
    # verbosity默认值为1，不限制完整结果，即单个用例成功输出’.’,失败输出’F’,错误输出’E’;
    # verbosity=2将输出完整的信息，verbosity=2是指测试结果的输出的详细程度，有0-6级，

if __name__ == '__main__':
    manager.run()
