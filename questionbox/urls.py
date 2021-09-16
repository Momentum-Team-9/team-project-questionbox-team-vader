from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as question_views
from core.views import QuestionListViewSet, AnswerListViewSet
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = SimpleRouter()
router.register("questions", QuestionListViewSet)
router.register("answers", AnswerListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# *get profile view/account
# **put question create
# *get question detail
# ***register new user