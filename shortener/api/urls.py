from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shortener.api.views import ShortURLViewSet

router = DefaultRouter()
router.register('', ShortURLViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
