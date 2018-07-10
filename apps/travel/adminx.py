import xadmin
from .models import Province,Scenic,Order

class ProvinceAdmin(object):
    # 显示的列
    list_display=['pname']
    #搜索的字段
    search_fields=['pname']
    #过滤
    list_filter=['pname']


class ScenicAdmin(object):
    list_display=['pname','sname','spicture','sdesc','sprice']
    search_fields=['pname','sname','spicture','sdesc','sprice']
    list_filter=['pname','sname','spicture','sdesc','sprice']


class OrderAdmin(object):
    list_display =['otime','omemnum','sname','oname','ophone','oremark','totalprice']
    search_fields =['sname','oname','ophone']
    list_filter =['otime','omemnum','sname','oname','ophone','oremark','totalprice']


xadmin.site.register(Province,ProvinceAdmin)
xadmin.site.register(Scenic,ScenicAdmin)
xadmin.site.register(Order,OrderAdmin)

