from rest_framework.routers import SimpleRouter
from django.urls import include
from django.urls import path

from app.api import viewsets

router = SimpleRouter()
router.register('', viewsets.TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
