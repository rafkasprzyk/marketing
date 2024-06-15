from django.shortcuts import render

# Create your views here.
def home(request):


    return render(request, 'base/home.html')


def blog(request):


    return render(request, 'base/blog.html')


def authors(request):


    return render(request, 'base/authors.html')


def quiz_all(request):


    return render(request, 'base/quiz_all.html')