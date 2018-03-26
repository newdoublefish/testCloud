from django.db import models
import datetime
# Create your models here.
class StubInfo(models.Model):
     SHIRT_SIZES = (
        ('0', '华为'),
        ('1', '英可瑞'),
        ('2', '麦格米特'),
     )    
     stub_text = models.CharField(u'铭牌编号',max_length=50,unique=True)
     sim_text = models.CharField(u'sim卡号',max_length=100)
     board_text = models.CharField(u'控制盒编号',max_length=50)
     ammeter1_text = models.CharField(u'电表1',max_length=50)
     ammeter2_text = models.CharField(u'电表2',max_length=50)
     gun1_text = models.CharField(u'枪1二维码',max_length=50)
     gun2_text = models.CharField(u'枪2二维码',max_length=50)
     gun_vendor_text = models.CharField(u'枪厂家',max_length=100)
     power_module_text=models.CharField(u'电源模块厂家',max_length=50,default="0",choices=SHIRT_SIZES)
     pub_date = models.DateTimeField('创建时间',default=datetime.datetime.now)
     def __str__(self):
        return "%s_%s"%(self.stub_text,self.sim_text)
     class Meta:
         verbose_name = "充电桩信息"
         verbose_name_plural = "充电桩信息"

class BoardInfo(models.Model):
     board_text = models.CharField(u'控制盒编号',max_length=100,unique=True)
     dcd_text = models.CharField(u'绝缘检测板编号',max_length=50)
     dcm_text = models.CharField(u'K60板编号',max_length=100)
     pwr_text = models.CharField(u'电源板编号',max_length=50)
     cpu_text = models.CharField(u'K64板编号',max_length=50)
     g4_text = models.CharField(u'4G编号',max_length=50)
     ddb_text = models.CharField(u'背板编号',max_length=50)
     dcr_text = models.CharField(u'继电器板编号',max_length=50)
     led_text = models.CharField(u'显示板编号',max_length=50)
     pub_date = models.DateTimeField('创建时间',default=datetime.datetime.now)
     def __str__(self):
        return "%s"%(self.board_text)
     class Meta:
         verbose_name = "控制盒信息"
         verbose_name_plural = "控制盒信息"

class TestType(models.Model):
    SHIRT_SIZES = (
        ('整机', '整机'),
        ('板级', '板级'),
        ('安规', '安规'),
    )
    name_text = models.CharField(max_length=50)
    def __str__(self):
        return self.name_text
    class Meta:
         verbose_name = "测试类型"
         verbose_name_plural = "测试类型"
    
class Record(models.Model):
    sn_text = models.CharField(u'测试编号',max_length=50,default="new record")
    testtype = models.ForeignKey(TestType, on_delete=models.CASCADE,verbose_name="测试类型")
    result_bool=models.BooleanField(u'测试结果',default=False)
    report_text=models.CharField(u'报表',max_length=250)
    pub_date= models.DateTimeField(u'测试时间')
    factory_text=models.CharField(u'工厂',max_length=50)
    person_text=models.CharField(u'测试人员',max_length=50)
    approved_bool=models.BooleanField(u'已审核',default=False)
    def __str__(self):
        return "%s_%s"%(self.testtype,self.pub_date)
    class Meta:
        verbose_name = "测试记录"
        verbose_name_plural = "测试记录"
