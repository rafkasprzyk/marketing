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


from django.shortcuts import render
from .forms import QuizForm


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
            return render(request, 'base/result.html', {'score': score, 'total': len(correct_answers)})
    else:
        form = QuizForm()
    return render(request, 'base/quiz_1.html', {'form': form})