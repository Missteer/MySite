from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    post_lists = []
    # for count,post in enumerate(posts):
    #     post_lists.append("No.{}".format(str(count)) + str(post) + "<hr>")
    #     post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    # return HttpResponse(post_lists)
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request,slug):
    template = get_template('post.html')

    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            now = datetime.now()
            html = template.render(locals())
            return HttpResponse(html)
    except:
        #发生意外的时候以 / 的方式直接返回首页
        return redirect('/')