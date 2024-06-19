from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('autorzy/', views.authors, name='authors'),
    path('quizy/', views.quiz_all, name='quiz_all'),
    path('blog/1/', views.blog_post_1, name='blog_post_1'),
    path('quizy/1', views.quiz_view, name='quiz_1'),

]