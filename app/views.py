from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
""" 业务逻辑都在viwes.py中,运行命令 python manage.py runserver 127.0.0.1:8000 """

def index(request):
    return HttpResponse("hello world!")

