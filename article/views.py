from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article


# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, my_args):
    get = Article.objects.all()[int(my_args)]
    msg = 'title = %s, category = %s, date_time= %s, content= %s' % (
        get.title, get.category, get.date_time, get.content)
    return HttpResponse(msg)


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now})
