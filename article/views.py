from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
# Create your views here.
def hometest(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

def detail(request,my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s" 
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

def datetest(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})