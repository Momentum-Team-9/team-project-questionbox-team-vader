from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as question_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', question_views.index, name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),    
    ] + urlpatterns
