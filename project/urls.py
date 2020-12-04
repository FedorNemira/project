from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


urlpatterns = [
    path('api/', include('poll.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('admin/', admin.site.urls),
]