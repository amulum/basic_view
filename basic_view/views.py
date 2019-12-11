from django.shortcuts import render, get_object_or_404
from .models import Blog, Mentee, Mentor
# Create your views here.

def index(request):
    return render (request, 'basic_view/home.html', {})

def blog(request):
    blog = Blog.objects.all()
    readmore = False

    return render (request, 'basic_view/blog.html', {'blogs':blog, 'readmore': readmore})

def mentee(request):
    mentee = Mentee.objects.all()
    return render (request, 'basic_view/mentee.html', {'mentees':mentee})

def mentor(request):
    data_mentor = Mentor.objects.all()
    return render (request, 'basic_view/mentor.html', {'mentors':data_mentor})

def author(request):
    return render (request, 'basic_view/author.html', {})

def input_blog(request):
    return render (request, "basic_view/input_blog.html", {})

def update(request):
    image_path  = request.POST['image_path']
    header      = request.POST['header']
    content     = request.POST['content']
    date        = request.POST['date']
    comment     = request.POST['comment']

    new = Blog(image_path=image_path, header=header, content=content, date=date, comment=comment)
    new.save()

    blog = Blog.objects.all()
    return render (request, 'basic_view/blog.html', {'blogs':blog})

def readmore(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render (request, 'basic_view/readmore.html', {'blog' : post})