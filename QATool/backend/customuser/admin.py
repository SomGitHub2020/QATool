from django.contrib import admin
from .models import Customuser # add this

class CustomuserAdmin(admin.ModelAdmin):  # add this
    list_display = ('user','password', 'firstname', 'lastname', 'email','role','countrycode','phone') # add this

# Register your models here.
admin.site.register(Customuser, CustomuserAdmin) # add this