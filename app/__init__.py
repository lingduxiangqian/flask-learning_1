from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config #从我们定义的config.py中引入config这个字典

bootstrap = Bootstrap() #先创建扩展的实例
mail = Mail()
moment = Moment()
db = SQLAlchemy() #初始化扩展

def create_app(config_name):
    app = Flask(__name__) #创建程序实例 
    #此处的__name__是一个全局变量， 它的值是代码所处的模块或包的名字，
    #Flask用这个参数决定程序的根目录， 以便稍后能找到相对于程序根目录的资源文件位置。
    app.config.from_object(config[config_name]) #本句作用是设置所有的config变量
    #通过config_name获取不同的Config子类对象，
    #app.config的from_object函数会对返回的Config对象的子类提取相关属性和值
    config[config_name].init_app(app) #调用init_app()这个静态方法对app进行其他的操作

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    #config中的init_app()方法是作者自定义的一个初始化方法，这个你去看看python静态方法就懂了；
    # 其实令人迷惑的是其他的bootstrap.init_app(app)类似这样的xx.init_app()，
    # 这个其实是这些Flask扩展自带的初始化方法，和你定义在config.py中的init_app()没有任何关系，
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # 附加使用蓝本路由和错误页面
    return app
