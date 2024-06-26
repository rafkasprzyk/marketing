from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('autorzy/', views.authors, name='authors'),
    path('quizy/', views.quiz_all, name='quiz_all'),
    path('blog/1/', views.blog_post_1, name='blog_post_1'),
    path('blog/2/', views.blog_post_2, name='blog_post_2'),
    path('blog/3/', views.blog_post_3, name='blog_post_3'),
    path('blog/4/', views.blog_post_4, name='blog_post_4'),
    path('blog/5/', views.blog_post_5, name='blog_post_5'),
    path('blog/6/', views.blog_post_6, name='blog_post_6'),
    path('blog/7/', views.blog_post_7, name='blog_post_7'),
    path('quizy/1/', views.quiz_view, name='quiz_1'),
    path('quizy/2/', views.quiz_view2, name='quiz_2'),
    path('quizy/3/', views.quiz_view3, name='quiz_3'),

]