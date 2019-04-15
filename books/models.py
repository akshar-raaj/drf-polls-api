from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


NULL_AND_BLANK = {'null': True, 'blank': True}


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, unique=True)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULL_AND_BLANK)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail', args=[self.id])
