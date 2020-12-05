from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/', include('poll.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)