from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as question_views
from core.views import QuestionListViewSet, AnswerListViewSet
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = SimpleRouter()
#router.register("questions", QuestionListViewSet)
router.register("answers", AnswerListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/questions/<int:pk>/detail/', question_views.question_detail),
    path('api/questions/', question_views.QuestionListViewSet.as_view(), name='question-list'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# *get profile view/account