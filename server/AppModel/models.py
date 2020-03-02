# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page
import datetime
from django.utils.html import format_html
from AppModel import *





class DeviceInfo(models.Model):
    id = models.CharField(max_length=200,verbose_name='设备ID',primary_key=True)
    device_name = models.CharField(max_length=200,verbose_name='设备名称')
    device_sn = models.CharField(max_length=200,verbose_name='设备编号')
    tenantId = models.CharField(max_length=200,verbose_name='租户Id')
    productId = models.CharField(max_length=200,verbose_name='产品Id')
    imei = models.CharField(max_length=200,verbose_name='IMEI号')
    deviceStatus = models.CharField(max_length=200,verbose_name='设备状态')
    autoObserver = models.CharField(max_length=200,verbose_name='是否订阅')
    createTime = models.CharField(max_length=200,verbose_name='创建时间')
    createBy = models.CharField(max_length=200,verbose_name='创建者')
    netStatus = models.CharField(max_length=200,verbose_name='信号强度')
    onlineAt = models.CharField(max_length=200,verbose_name='最后上线时间')
    offlineAt = models.CharField(max_length=200,verbose_name='最后离线时间')
    isOnline = models.CharField(max_length=200,verbose_name='是否已上线')
    deviceVoltageStatus = models.CharField(max_length=200,verbose_name='设备电压状态')
    lastUploadTime = models.CharField(max_length=200,verbose_name='上报时间')
    # userinfo = models.ManyToManyField(UserInfo,null=True,blank=True,verbose_name='业主姓名')
    companyinfo = models.ForeignKey('CompanyInfo',on_delete=models.CASCADE,null=True,blank=True,verbose_name='联网单位')
    construction_worker = models.CharField(max_length=200,verbose_name='施工人员')
    construction_createtime = models.DateField(default=datetime.date.today,verbose_name='施工时间')
    construction_image = models.ImageField(u'施工图片',null=True, blank=True, upload_to='contruction_image')
    install_location = models.CharField(max_length=200,verbose_name='安装位置')
    device_address = models.CharField(max_length=200,verbose_name='设备地址')
    

    
    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'
    
    def profile(self):
        return str()
    
    def __str__(self):
        return self.device_name

