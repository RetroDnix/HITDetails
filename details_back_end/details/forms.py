from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, IntegerField ,TextAreaField, SubmitField, MultipleFileField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('用户名：', validators=[DataRequired()])
    password = PasswordField('密码：', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('保持登录状态')
    submit = SubmitField('登录')

class SendForm(FlaskForm):
    Togroup = StringField('目标组织')
    Touser = StringField('目标用户')
    Sender = StringField('发信人')
    Title = StringField('标题')
    Text = TextAreaField('正文')
    submit = SubmitField('发送')

class ModifyForm(FlaskForm):
    Touser = StringField('目标用户')
    Togroup = IntegerField('目标组织')
    au1 = BooleanField("发送消息")
    au2 = BooleanField("修改下级管理员的权限")
    au3 = BooleanField("修改同级管理员的权限")
    au4 = BooleanField("修改组织关系")
    au5 = BooleanField("增加/删除成员")
    submit = SubmitField('修改')

class EditExtendForm(FlaskForm):
    Father = IntegerField('父亲组织')
    submit = SubmitField('修改')

class CreateForm(FlaskForm):
    GroupName = StringField('组名',validators=[DataRequired(), Length(1, 128)])
    submit = SubmitField('创建')

class EditMemberForm(FlaskForm):
    Method = RadioField('操作',choices=[('add','添加组员'),('rm','删除组员')])
    Touser = StringField('目标用户')
    Togroup = IntegerField('目标组织')
    submit = SubmitField('修改')
