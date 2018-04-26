from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Email(models.Model):
    email = models.TextField(default="")


class PriceData(models.Model):
    time = models.DateTimeField()
    price = models.TextField(default="")

    def __str__(self):
        return self.price


class XMRData(models.Model):
    time = models.DateTimeField()
    price = models.TextField(default="")

    def __str__(self):
        return self.price
