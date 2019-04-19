#创建蓝本
# 和在单一脚本文件中编写小型web程序不同，
# 我们只有在调用create_app后程序实例app才存在，
# 此时再用app定义路由显然来不及， 这是我们可以用蓝本定义路由， 路由处于休眠状态， 
# 然后再在create_app函数中把蓝本注册到程序实例app上， 路由就注册到了程序实例上：
from flask import Blueprint
main = Blueprint('main',__name__) #定义蓝本， 第一个参数为蓝本名， 第二个参数代码所在模块或者包
from . import views,errors #把蓝本与路由和错误处理程序关联起来代表
#from . import代表使用相对路径导入，即从当前项目中寻找需要导入的包或函数
