from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField("Fecha de publicación")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)

