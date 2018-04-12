from django.contrib import admin
from .models import StubInfo,BoardInfo,TestType,Record
# Register your models here.
admin.site.site_header = "广州万城万充新能源科技"
class StubInfoAdmin(admin.ModelAdmin):
    list_display=('stub_text','gun_vendor_text','power_module_text','pub_date')
    search_fields=('stub_text',)

class RecordAdmin(admin.ModelAdmin):
    list_display=('sn_text','testtype','report_text','pub_date','approved_bool')
    search_fields=('sn_text',)

class BoardInfoAdmin(admin.ModelAdmin):
    list_display=('board_text','pub_date')
    search_fields=('board_text',)
admin.site.register(StubInfo,StubInfoAdmin)
admin.site.register(BoardInfo,BoardInfoAdmin)
#admin.site.register(TestType)
admin.site.register(Record,RecordAdmin)
