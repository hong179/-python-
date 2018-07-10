from django.urls import path,re_path
from .views import ScenicListView,ScenicDetailView,CompProfView,ContactUsView,AddOrderView,OrderView

app_name='travel'

urlpatterns = [
    #景点列表,name指templates
    path('senics/list',ScenicListView.as_view(),name='scen_list'),
    #景点详情
    re_path('senics/detail/(?P<scen_id>\d+)/',ScenicDetailView.as_view(),name='scen_detail'),



    #添加预约
    path('order/add',AddOrderView.as_view(),name='order_add'),


    #预约详情
    path('order/list',OrderView.as_view(),name="order_list"),


    #公司简介
    path('comp/prof',CompProfView.as_view(),name='comp_prof'),
    #联系我们
    path('contact/us',ContactUsView.as_view(),name='contact_us'),

]