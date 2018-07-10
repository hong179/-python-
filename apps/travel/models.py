from django.db import models


# Create your models here.
#城市表
class Province(models.Model):
    pname=models.CharField('城市',max_length=100,default='')

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.pname

#景点表
class Scenic(models.Model):
    pname=models.ForeignKey(Province,verbose_name='城市',on_delete=models.CASCADE)
    sname=models.CharField('景点名称',max_length=100,default='')
    spicture=models.ImageField('景区图片',upload_to='simage/',max_length=100)
    sdesc=models.CharField('景区介绍',max_length=500,default='')
    sprice=models.IntegerField('景区价格',default=0)


    class Meta:
        verbose_name="景区详情"
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.sname


#预约表
class Order(models.Model):
    otime=models.DateField('预约时间')
    omemnum=models.IntegerField('预约人数',default=1)
    sname=models.CharField('景区名称',max_length=100,default='')
    oname=models.CharField('联系人',max_length=100,default='')
    ophone=models.CharField('联系电话',max_length=11,default='')
    oremark=models.CharField('备注',max_length=200,default='')
    totalprice=models.IntegerField('总价格',default=0)

    class Meta:
        verbose_name='预约详情'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.oname