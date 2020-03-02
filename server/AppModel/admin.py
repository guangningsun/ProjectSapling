# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
import logging,json,datetime
import AppModel.aeptools as aeptools
from django.utils.html import format_html
from django import forms
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
# from django.utils.safestring import mark_safe
from django.utils.html import format_html,escape, mark_safe
from django.http import HttpResponse, HttpResponseRedirect


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("tjctwl.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin):
    list_display=['id','login_name','username','user_permission','phone_number','create_time','user_sex','user_age','description','get_devices']
    #list_editable = ['login_name','username','user_permission','phone_number','user_sex','user_age','description']
    #search_fields =('login_name','username','user_permission','phone_number','create_time','user_sex','user_age','description')
    #fieldsets = [
     #   ('用户数据', {'fields': ['login_name','username','user_permission','phone_number','create_time','user_sex','user_age','description'], 'classes': ['collapse']}),
    #]
    def get_devices(self, obj):
             return [bt.device_sn for bt in obj.device_sn.all()]
    get_devices.short_description ='所有设备'
    filter_horizontal = ('device_sn',)
    def save_model(self, request, obj, form, change):
        for i in range(0,len(obj.device_sn.get_queryset())):
            device_obj = obj.device_sn.get_queryset()[i]
            DeviceInfo.objects.filter(id=device_obj.id).update(isOnline='0')
        try:
            pass
        except:
            pass
        super().save_model(request, obj, form, change)