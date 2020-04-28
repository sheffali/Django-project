"""online_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from test1 import views

urlpatterns = [
url(r'^index/',views.index,name='index'),
url(r'^home',views.home,name='home'),
url(r'^log/',views.reg,name='reg'),
path('admin/', admin.site.urls),
url(r'^formpage/',views.testform,name="testform"),
url(r'^regist/',views.registration,name='registration'),
url(r'^act1/',views.act1,name='act1'),
url(r'^act3/',views.act3,name='act3'),
url(r'^act4/',views.act4,name='act4'),
url(r'^index3/',views.index3,name='index3'),
url(r'^index2/',views.index2,name='index2'),
url(r'^index4/',views.index4,name='index4'),
url(r'^act5/',views.act5,name='act5'),
url(r'^index5/',views.index5,name='index5'),
]
