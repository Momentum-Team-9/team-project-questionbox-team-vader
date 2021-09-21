from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as question_views
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/questions/<int:pk>/', question_views.QuestionDetailsViewSet.as_view(), name='question-detail'),
    path('api/questions/', question_views.QuestionListViewSet.as_view(), name='question-list'),
    path('api/answers/new/', question_views.AddAnswerViewSet.as_view(), name='answer-new'),
    path('auth/users/me', question_views.UserQuestionListViewSet.as_view(), name='user-profile'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# *get profile view/account