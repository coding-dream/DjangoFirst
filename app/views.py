from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

""" 业务逻辑都在viwes.py中,运行命令 python manage.py runserver 127.0.0.1:8000 """

@csrf_exempt
def index(request):
    # return HttpResponse("hello world!")
    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username + password)
    else:
        print("user is error")
    return render(request,"index.html") # <!-- 在 Django 模板中 {{}} 表示引用一个变量， {%%} 表示代码调用。 -->

@csrf_exempt
def list(request):
    address = [
        {'name': '张三', 'address': '地址一'},
        {'name': '李四', 'address': '地址二'}
    ]
    return render_to_response('result.html', {'address': address})



