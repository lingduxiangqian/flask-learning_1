import os
basedir = os.path.abspath(os.path.dirname(__file__)) #返回本脚本所在目录

class Config: #配置基类： 通用配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' #设置密钥， web表单防止CSRF攻击
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #请求后数据库的改动会自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = False #为了消除警告， 具体作用不明
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  #邮件主题前缀
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>' #发件人
    FLASKY_ADMIN = os.environ.get('FASKY_ADMIN') #程序管理员邮箱地址
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config): #开发配置类
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):#测试配置类
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'data.sqlite')

class ProductionConfig(Config):  #生产配置类
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

#创建基类Config来保存通用配置 其他的各环境使用不同的配置 再用一个字典提供选择
config = {
    'developmet' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}

