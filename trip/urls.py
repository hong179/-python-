"""trip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin

from django.urls import path,include,re_path
from django.views.generic import TemplateView
from users.views import LoginView,LogoutView
from users.views import RegisterView,ActiveUserView,IndexView
from users.views import ForgetPwdView,ResetView,ModifyPwdView
from trip.settings import MEDIA_ROOT
from django.views.static import serve


urlpatterns = [
    #urls中，通过类的as_view方法，调用这个View类
    path('xadmin/', xadmin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/',ResetView.as_view(),name='reset_pwd'),
    path('modify_pwd/',ModifyPwdView.as_view(),name='modify_pwd'),
    #处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    path('travel/',include('travel.urls',namespace='travel')),
    #path('users/',include('users.url',namespace='users')),


]