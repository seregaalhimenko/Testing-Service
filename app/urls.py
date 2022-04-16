from django.urls import path, include
from app.routers import routers


urlpatterns = [
    path('', include(routers.router.urls)),
]
