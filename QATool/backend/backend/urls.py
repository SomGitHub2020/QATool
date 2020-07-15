"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers                    # add this
from customuser import views1 
from qaconfig import views

router = routers.DefaultRouter()                      # add this
router.register(r'customusers', views1.CustomuserView, 'customuser')

#router1 = routers.DefaultRouter()                      # add this
router.register(r'qaconfigs', views.QaconfigView, 'qaconfig')

#save
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    url(r'^',views1.ReactAppView.as_view()),
#    path('apicust/', include(router.urls)),
#    url(r'^rest-auth/', include('rest_auth.urls')),
#    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#    url(r'^account/', include('allauth.urls')),
#    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]

