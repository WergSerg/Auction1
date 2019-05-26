from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

#Form = flask.ext.wtf


class LoginForm(Form):
    openid = TextField('openid')
    remember_me = BooleanField('remember_me', default=False)


