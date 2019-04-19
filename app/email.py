from threading import Thread # 导入Python标准库中的Thread模块
from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)  #发送邮件


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to]) #创建邮件
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs) #定义邮件内容
    thr = Thread(target=send_async_email, args=[app, msg]) # 创建一个线程
    #创建线程thr,使用threading.Thread()方法，
    #target:后加需要线程去执行的方法名,
    # args: 线程执行方法接收的参数，该属性是一个元组，如果只有一个参数也需要在末尾加逗号。
    thr.start() # 启动刚刚创建的线程
    return thr
