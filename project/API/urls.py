from django.urls import include, path
from rest_framework import routers
from API.views import CandidateViewSet

router = routers.DefaultRouter()

router.register('candidate',CandidateViewSet, basename='candidate')

urlpatterns = [
    path('', include(router.urls)),
]