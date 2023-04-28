from django.db import models
from django.contrib.auth import get_user_model

class Books(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    file = models.FileField(upload_to='files/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    book_author = models.CharField(max_length=150)
    def __str__(self):
        return self.title