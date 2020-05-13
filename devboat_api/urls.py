"""devboat_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('users.urls')),
    path('api/v1/',include('education.urls')),
    path('api/v1/',include('interests.urls')),
    path('api/v1/',include('job.urls')),
    path('api/v1/',include('projects.urls')),
    path('api/v1/',include('skills.urls')),
    path('api/v1/',include('connections.urls')),
    path('api/v1/',include('requests.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/auth/', include('rest_auth.urls'))
]
