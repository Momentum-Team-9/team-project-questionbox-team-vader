from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as question_views
from core.views import QuestionListViewSet, AnswerListViewSet
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = SimpleRouter()
router.register("api/questions", QuestionListViewSet)
router.register("api/answers", AnswerListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', question_views.QuestionListViewSet, name='home'),
    path('questions/<int:pk>/', question_views.QuestionDetailsViewSet.as_view,()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]+ router.urls