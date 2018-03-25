from django.db import models

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
     def __str__(self):
        return "%s_%s"%(self.stub_text,self.sim_text)

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
     def __str__(self):
        return "%s"%(self.board_text)

class TestType(models.Model):
    SHIRT_SIZES = (
        ('整机', '整机'),
        ('板级', '板级'),
        ('安规', '安规'),
    )
    name_text = models.CharField(max_length=50)
    def __str__(self):
        return self.name_text
    
class Record(models.Model):
#    type=models.IntegerField(default=0)
    sn_text = models.CharField(max_length=50,default="new record")
    testtype = models.ForeignKey(TestType, on_delete=models.CASCADE)
    result_bool=models.BooleanField(default=False)
    report_text=models.CharField(max_length=250)
    pub_date= models.DateTimeField('report product')
    factory_text=models.CharField(max_length=50)
    person_text=models.CharField(max_length=50)
    approved_bool=models.BooleanField(default=False)
    def __str__(self):
        return "%s_%s"%(self.testtype,self.pub_date)
