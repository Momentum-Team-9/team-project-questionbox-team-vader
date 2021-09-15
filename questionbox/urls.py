from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from core import views as question_views
from api import views
from api.views import QuestionList
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

question_router = SimpleRouter()
question_router.register("api/questions", QuestionList, basename="question")

urlpatterns = [
    path('', include('questionbox.urls')),
    path('', question_views.index, name='index'),
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]+ question_router.urls