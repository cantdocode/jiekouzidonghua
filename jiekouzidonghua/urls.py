"""jiekouzidonghua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from TestJKZDH.views import *
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome',welcome),
    path('home',home),
    # re_path("^/child/(?P<eid>.+)", child)
    # path(r"^child/(?P<eid>.+)/(?P<oid>.*)/$", child),
    url(r"^child/(?P<eid>.+)",child),  # 返回子页面
#     这是标准的正则写法。目的是获取url中的这俩个变量。
# 这个url后面的俩段，并不是写死的一成不变的。而是一个变量，对应的是我们welcome.html中的 whichHTML 和  oid
#   <int:xx>  能用
    url('login',login)
]
