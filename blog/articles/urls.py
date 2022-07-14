from django.urls import path
from . import views
from .views import ArticleUpdate, ArticleDelete
app_name = 'articles'

urlpatterns = [
    path('articles_list/', views.articles_list, name="list"),
    path('create_article/', views.create_article, name='create'),
    path('<slug:slug>/', views.article_details, name="detail"),
    path('article-update/<int:pk>', ArticleUpdate.as_view(), name='article_update'),
    path('article-delete/<int:pk>', ArticleDelete.as_view(), name='article-delete'),
]
