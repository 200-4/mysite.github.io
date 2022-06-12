import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    def __str__(self):
       question_text = models.CharField(max_length=200)
       return self.question_text
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    def __str__(self):
        choice_text = models.CharField(max_length=200)
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
