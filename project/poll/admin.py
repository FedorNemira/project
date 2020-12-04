from django.contrib import admin
from poll.models import UserProfile, Poll, Question, QuestionOption, UserAnswer


admin.site.register(UserProfile)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(UserAnswer)



