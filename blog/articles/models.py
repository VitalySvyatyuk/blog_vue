from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    user = models.CharField(max_length=100, default="anonymous")
    created = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

