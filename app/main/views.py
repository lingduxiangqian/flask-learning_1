from datetime import datetime
from flask import session, render_template, url_for, redirect, current_app

from . import main
from . forms import NameForm
from ..models import User
from .. import db
from ..email import send_email
"""
相对导入其他格式
from . import C   导入包内的C模块（A.B.C）
from .. import E  导入上级目录的E模块（A.E）
from ..E import F  导入上级目录的E模块的F属性(A.E.F)
"""

@main.route('/', methods=['GET', 'POST'])  #视图函数
def index():
    form = NameForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
 
    return render_template('index.html', form=form,name=session.get('name'), 
        known=session.get('known',False), current_time=datetime.utcnow())
