"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from app import xls_action
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index),# 类似SpringMVC的@Controller注解  我的路由，重点是引号中的正则表达式和 views.index 函数(还实现index 函数)
    url(r'^$', views.index), # 匹配空串(也就是形如: http://localhost:8000/,如果这时 web server 已经启动了，那么直接刷新页面就行了。)
    url(r'^list/$', views.list),
    url(r'^xls/(?P<filename>\w+)/$', xls_action.download), # (?P<filename>\w+) 这是一个将解析结果起名为 filename 的正则表达式,还记得吗？我们的链接是写成 /xls/address/ ，因此上面实际上会变成对 xls_test.output(filename='address') 的调用。
]
