from flask import redirect,session,url_for,render_template,request

from details import app
from details.forms import *
from details.methods import *

# 开始界面,没什么用
@app.route("/")
def index():
    f = open("flask.log","a")
    f.write('''\n---------------------------\nMethod:%s\nHearders:\n%s\nArgs:%s\nForm:%s\n---------------------------\n'''%(request.method,request.headers,request.args,request.form))
    f.close()
    return render_template("startpage.html")

# 登出界面,作用是把session删掉,实现登出
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))