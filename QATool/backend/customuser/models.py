from django.db import models
    # Create your models here.

    # add this
class Customuser(models.Model):
    user = models.CharField(max_length=120,primary_key=True)
    password = models.CharField(max_length=120)
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    countrycode = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    

    def _str_(self):
        return self.user