from django.contrib import admin
from .models import Qaconfig # add this

class QaconfigAdmin(admin.ModelAdmin):  # add this
    list_display = ('qaconnid', 'systemtype', 'ipaddress', 'port', 'adminuser', 'adminpass', 'sysid', 'client', 'githuburl', 'triggerrate', 'triggeruom')

# Register your models here.
admin.site.register(Qaconfig, QaconfigAdmin) # add this