from rest_framework import serializers

from blog.articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = ['__all__']
        