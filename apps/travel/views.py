from django.shortcuts import render
from .models import Province,Scenic,Order
from .forms import OrderForm
from django.views.generic import View
#对对象的复杂查询
from django.db.models import Q
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponse



class ScenicListView(View):
    '''景点列表'''
    def get(self,request):
        #所有景点
        all_scen=Scenic.objects.all()
        #所有城市
        all_prov=Province.objects.all()
        #景点搜索功能
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            #在name字段进行操作，做like语句的操作。i代表不区分大小写
            #or操作使用Q
            all_scen=all_scen.filter(Q(sname__icontains=search_keywords ) | Q(sdesc__iconcontains=search_keywords))
        #城市筛选
        prov_id=request.GET.get('pname','')
        if prov_id:
            all_scen=all_scen.filter(prov_id=int(prov_id))

        #有多少景点
        senc_nums=all_scen.count()
        #对景点进行分页
        #尝试获取前台get传递过来的page参数
        #如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page=1
        #这里指从allscen中取出8个，每页显示8个
        p=Paginator(all_scen,8,request=request)
        scens=p.page(page)

        return render(request,'scen_list.html',{
            'all_scen':scens,
            'all_prov':all_prov,
            'senc_nums':senc_nums,
            'prov_id':prov_id,
        })

class ScenicDetailView(View):

    def get(self,request,scen_id):


        #根据id找到景点
        scenic=Scenic.objects.get(id=int(scen_id))

        return render(request,'scen_detail.html',{
            'scenic':scenic,

        })

class OrderView(View):
    def get(self,request):
        # 所有预约
        all_scen = Scenic.objects.all()
        all_ord=Order.objects.all()
        scen_id = request.GET.get('sname', '')

        if scen_id:
            all_scen = all_scen.filter(scen_id=int(scen_id))
        return render(request,'order_list.html',{
            'all_ord':all_ord,
            'all_scen': all_scen,
            'scen_id': scen_id,

        })




class AddOrderView(View):
    def get(self,request):
        all_scen = Scenic.objects.all()
        return render(request,'order_add.html',{
            'all_scen':all_scen,
        })


    def post(self,request):
        order_form=OrderForm(request.POST)
        if order_form.is_valid():

            order_form.save()
            return render(request,'order_add.html')
            #如果保存成功，返回json字符串，后面content_type是告诉浏览器返回的数据类型
            #return HttpResponse('{"status":"success"}',content_type='application/json')
        else:
            return render(request, '404.html')
            #如果保存失败，返回json字符串，并将form的报错信息通过msg传递到前端 404.html

            #return HttpResponse('{"status":"fail","msg":"添加出错"}',content_type="application/json")




class CompProfView(View):
    def get(self,request):
        return render(request,'comp_prof.html')

class ContactUsView(View):
    def get(self,request):
        return render(request,'contact_us.html')