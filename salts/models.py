from __future__ import unicode_literals

from django.db import models


class HostInfoModel(models.Model):
    hostname=models.CharField(max_length=100)
    ipaddress=models.CharField(max_length=200)
    cpuinfo=models.CharField(max_length=50)
    meminfo=models.CharField(max_length=50)
    group=models.CharField(max_length=50)
    osinfo=models.CharField(max_length=20)
    area=models.CharField(max_length=100)
    usage=models.CharField(max_length=200)
    class Meta:
	db_table='ops_host_info'
	
