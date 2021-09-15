from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as question_views

urlpatterns = [
    path('', question_views.index, name='index'),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('^auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]