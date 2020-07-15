from django.db import models
    # Create your models here.

    # add this
class Qaconfig(models.Model):
    
    #systemname = models.CharField(max_length=10)
    #systemendpoint = models.CharField(max_length=10)
    #user = models.CharField(max_length=10)
    #password = models.CharField(max_length=10)

    qaconnid = models.CharField(max_length=50, null=True)
    systemtype = models.CharField(max_length=10, null=True)
    ipaddress = models.CharField(max_length=15, null=True)
    port = models.CharField(max_length=5, null=True)
    adminuser = models.CharField(max_length=25, null=True)
    adminpass = models.CharField(max_length=30, null=True)
    sysid = models.CharField(max_length=2, null=True)
    client = models.CharField(max_length=3, null=True)
    githuburl = models.CharField(max_length=100, null=True)
    triggerrate = models.CharField(max_length=3, null=True)
    triggeruom = models.CharField(max_length=10, null=True)

    def _str_(self):
        return self.qaconnid