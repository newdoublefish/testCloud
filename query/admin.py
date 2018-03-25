from django.contrib import admin
from .models import StubInfo,BoardInfo,TestType,Record
# Register your models here.
admin.site.register(StubInfo)
admin.site.register(BoardInfo)
#admin.site.register(TestType)
admin.site.register(Record)
