from django.urls import path, include, re_path


# from . import views

# app_name = 'app'
urlpatterns = [
    path('base-auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]