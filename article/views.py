#coding=utf-8
'''
1.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")

def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)
'''

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
#2
'''
def home(request):
    return HttpResponse("Hello World, Django")
'''
#4
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

'''
#3
def test(request) :
    #render()函数中第一个参数是request 对象, 第二个参数是一个模板名称，第三个是一个字典类型的可选参数. 它将返回一个包含有给定模板根据给定的上下文渲染结果的 HttpResponse对象。
    return render(request, 'test.html', {'current_time': datetime.now()})

'''
