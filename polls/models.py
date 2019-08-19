import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published', null=True)
    author = models.CharField(max_length=200, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

    # def was_published_recently(self):
        # now = timezone.now()
        # return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # def choices(self):
        # if not hasattr(self, '_choices'):
            # self._choices = self.choice_set.all()
        # return self._choices

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
