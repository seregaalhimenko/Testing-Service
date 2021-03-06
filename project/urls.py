"""project URL Configuration
    path('', Home.as_view(), name='home')
    path('blog/', include('blog.urls'))
"""
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include, re_path
from.yasg import urlpatterns as doc_urls


urlpatterns = [
    path('accounts/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]

urlpatterns += doc_urls

urlpatterns += [
    path('', lambda request: redirect('doc/', permanent=True)),
]
