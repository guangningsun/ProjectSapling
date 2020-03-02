from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view

class InstallDeviceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    deviceStatus = serializers.CharField(required=False)
    construction_image = serializers.CharField(required=False)

    class Meta:
        model = DeviceInfo
        fields = ('id','construction_createtime','deviceStatus','construction_image','device_sn','device_name',\
            'construction_worker','install_location','device_address')

