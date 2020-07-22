from django.contrib import admin
from .models import QALog # add this

class QALogAdmin(admin.ModelAdmin):  # add this
    list_display = ('SystemType','QAConnID','QACreatedDate','JIRALogFlag','QALog','QALoggedDate','ObjectName','ObjectPath','DevelopedBy') # add this

    # Register your models here.
admin.site.register(QALog, QALogAdmin) # add this