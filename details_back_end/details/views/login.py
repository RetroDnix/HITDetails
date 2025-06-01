from flask import redirect,session,url_for,render_template

from details import app
from details.forms import *
from details.methods import *

# 登录界面
@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # remember = form.remember.data
        if username == 'admin' and password == 'admintest':
            session["logged_in"] = True
            session['id'] = 'admin'
            # if remember:
            #     session.permanent = True
            return redirect(url_for('overview'))
        else:
            return render_template("login.html",form = form,text='Wrong username or password!')
    return render_template("login.html",form = form,text='HITDetails后台')

# 登出界面,作用是把session删掉,实现登出
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))