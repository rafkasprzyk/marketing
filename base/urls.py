from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('autorzy/', views.authors, name='authors'),
    path('quizy/', views.quiz_all, name='quiz_all'),

]