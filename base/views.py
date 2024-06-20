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


def blog_post_1(request):


    return render(request, 'base/blog_post_1.html')


def blog_post_2(request):


    return render(request, 'base/blog_post_2.html')


def blog_post_3(request):


    return render(request, 'base/blog_post_3.html')



def blog_post_4(request):


    return render(request, 'base/blog_post_4.html')


def blog_post_5(request):


    return render(request, 'base/blog_post_5.html')



def blog_post_6(request):


    return render(request, 'base/blog_post_6.html')



from django.shortcuts import render
from .forms import QuizForm, QuizForm2, QuizForm3


def quiz_view(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            score = 0
            correct_answers = {
                'Q1': False,
                'Q2': True,
                'Q3': False,
                'Q4': True,
                'Q5': False,
                'Q6': False,
                'Q7': True,
                'Q8': True,
                'Q9': False,
                'Q10': False,
            }
            for question, correct in correct_answers.items():
                if form.cleaned_data[question] == str(correct):
                    score += 1
            return render(request, 'base/result.html', {'score': score, 'total': len(correct_answers), 'title': 'pr'})
    else:
        form = QuizForm()
    return render(request, 'base/quiz_1.html', {'form': form})


def quiz_view2(request):
    if request.method == 'POST':
        form = QuizForm2(request.POST)
        if form.is_valid():
            score = 0
            correct_answers = {
                'Q1': False,
                'Q2': True,
                'Q3': True,
                'Q4': True,
                'Q5': True,
                'Q6': True,
                'Q7': False,
                'Q8': False,
                'Q9': False,
                'Q10': True,
            }
            for question, correct in correct_answers.items():
                if form.cleaned_data[question] == str(correct):
                    score += 1
            return render(request, 'base/result.html', {'score': score, 'total': len(correct_answers), 'title': 'marketing'})
    else:
        form = QuizForm2()
    return render(request, 'base/quiz_2.html', {'form': form})


def quiz_view3(request):
    if request.method == 'POST':
        form = QuizForm3(request.POST)
        if form.is_valid():
            score = 0
            correct_answers = {
                'Q1': True,
                'Q2': False,
                'Q3': True,
                'Q4': True,
                'Q5': False,
                'Q6': True,
                'Q7': True,
                'Q8': True,
                'Q9': True,
                'Q10': True,
            }
            for question, correct in correct_answers.items():
                if form.cleaned_data[question] == str(correct):
                    score += 1
            return render(request, 'base/result.html', {'score': score, 'total': len(correct_answers), 'title': 'strategie'})
    else:
        form = QuizForm3()
    return render(request, 'base/quiz_3.html', {'form': form})