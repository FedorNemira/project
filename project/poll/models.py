from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ("manager", "Manager"),
        ("registred_user", "Registred user"),
        ("anonymous_user", "Anonymous user"),
    )   
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    user_uid = models.CharField(max_length=50, null=True, blank=True, unique=True)
    def __str__(self):
        s = self.user_type
        if self.user:
            s += f' {self.user}'
        if self.user_uid:
            s += f' {self.user_uid}'
        return s


class Poll(models.Model):
    user_profile = models.ForeignKey('poll.UserProfile', on_delete=models.CASCADE)
    poll_name = models.CharField(max_length=50)
    poll_date_start = models.DateTimeField(auto_now_add=True)
    poll_date_end = models.DateTimeField(null=True, blank=True)
    poll_description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    QUESION_TYPE_CHOICES = (
        ("text_answer", "Text answer"),
        ("one_choice", "One choice"),
        ("multiple_choice", "Multiple choice"),
    )
    user_profile = models.ForeignKey('poll.UserProfile', on_delete=models.CASCADE)   
    question_text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=255, choices=QUESION_TYPE_CHOICES)
    def __str__(self):
        return f'{self.question_text}, {self.question_type}'

    
class QuestionOption(models.Model):
    question = models.ForeignKey('poll.Question', on_delete=models.CASCADE)
    question_option_name = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.question_option_name}'


class UserAnswer(models.Model):
    user_profile = models.ForeignKey('poll.UserProfile', on_delete=models.CASCADE)
    question = models.ForeignKey('poll.Question', on_delete=models.CASCADE)
    text_answer = models.CharField(max_length=500, null=True, blank=True)
    question_option = models.ManyToManyField('poll.QuestionOption')
    def __str__(self):
        s = str(self.question)
        if self.text_answer:
            s += f' {self.text_answer}'
        return s
        



