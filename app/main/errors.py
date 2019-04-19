from flask import render_template #Flask通过render_template()函数来实现模板的渲染
from . import main 

#主程序的errorhandler
@main.app_errorhandler(404) #404错误处理程序
def page_not_found(e):
    return render_template('404.html'),404

@main.app_errorhandler(500) #500错误处理程序
def internal_server_error(e):
    return render_template('500.html'),500
