from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Hblog

def home(request):
    blog = Hblog.objects
    return render(request, 'home.html',{'blog':blog})

def detail(request, blog_id):
    details = get_object_or_404(Hblog,pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request,'new.html')

def create(request):
    blog= Hblog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.date = timezone.datetime.now()
    blog.save() #객체.delete()삭제..
    return redirect ('/blog/' + str(blog.id))
