from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from poll.models import UserProfile
import uuid


class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        user = request.user

        try:
            user_profile = UserProfile.objects.get(user=user) #Если зашел как джанговский user 
        except Exception as e:
            print(e)
            user_profile = None #если юзер не аторизовать то он записывается как none 

        if user_profile:
            request.profile = user_profile
            request.role = user_profile.user_type #цепляет user_type из базы 
            request.user_uid = None
        else:
            user_uid = request.session.get('user_uid') #определяем user_uid(для удобства)
            try:
                user_profile = UserProfile.objects.get(user_uid=user_uid)
            except:
                user_profile = None 

            if not user_profile:
                request.session['user_uid'] = user_uid = str(uuid.uuid4()) #генерит уникальный ключ uid 
                user_profile = UserProfile()
                user_profile.user_type = "anonymous_user"
                user_profile.user_uid = user_uid 
                user_profile.save()

            request.profile = user_profile
            request.role = "anonymous_user"
            request.user_uid = user_uid

        response = self.get_response(request) #стандартная заглушка 

        return response

        #всё, что кроме 12-39 это стандартная джанговская тема 