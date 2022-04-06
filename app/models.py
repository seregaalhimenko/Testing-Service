from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Theme(models.Model):
    name = models.CharField(max_length=500)
    theory = models.TextField()

    def __str__(self):
        return self.name


class Test(models.Model):
    # creator = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Choice(models.Model):
    value = models.BooleanField()
    text = models.TextField()
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.text


class AnswerTracker(models.Model):
    ''' Model for storing customer's answers '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(
        Choice, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.test} '
