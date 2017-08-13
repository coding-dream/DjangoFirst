from django.db import models

# Create your models here.
""" 
    类似Java Hibernate orm框架 
    执行命令
    python manage.py makemigrations
    python manage.py migrate
"""
class UserBean(models.Model):
    name = models.CharField(max_length=20)  # 类属性，
    age = models.IntegerField()