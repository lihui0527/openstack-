from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from .models import Post

# Create your views here.
def index(request):
    posts =Post.objects.all()
    now =datetime.now()
    template=get_template('myblogs/index.html')
    html=template.render(locals())
#    post_lists=[]
#    for count,post in enumerate(posts,1):
 #       post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
    return HttpResponse(html)
def show_post(request,slug):
    template = get_template('myblogs/post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post !=None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
