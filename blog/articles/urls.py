from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('articles_list/', views.articles_list, name= "list"),
    path('create_article/', views.create_article, name='create'),
    path('<slug:slug>/', views.article_details, name = "detail"),
]
