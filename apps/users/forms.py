from django import forms
from captcha.fields import CaptchaField

#登录表单验证
class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    '''注册验证表单'''
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True,min_length=5)
    #验证码，字段里面可以自定义错误提示信息
    captcha=CaptchaField(error_messages={'invalid':'验证码错误'})


class ForgetPwdForm(forms.Form):
    '''忘记密码'''
    email=forms.EmailField(required=True)
    captcha=CaptchaField(error_messages={'invalid':'验证码错误'})

'''重置密码'''
class ModifyPwdForm(forms.Form):
    password1=forms.CharField(required=True,min_length=5)
    password2=forms.CharField(required=True,min_length=5)


