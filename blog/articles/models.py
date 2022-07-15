from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title

    # Pierwsze 120 liter tekstu, który bedzie wyswietlony na głównej stronie
    def snippet(self):
        return self.body[:120] + "     Zobacz dalszą część artykułu!"
