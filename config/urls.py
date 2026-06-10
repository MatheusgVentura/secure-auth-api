"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request):
    return Response(
        {
            "name": "Django Secure Auth API",
            "version": "v1",
            "endpoints": {
                "health": request.build_absolute_uri("/api/v1/health/"),
                "register": request.build_absolute_uri("/api/v1/auth/register/"),
                "login": request.build_absolute_uri("/api/v1/auth/login/"),
                "token_refresh": request.build_absolute_uri(
                    "/api/v1/auth/token/refresh/"
                ),
                "logout": request.build_absolute_uri("/api/v1/auth/logout/"),
                "me": request.build_absolute_uri("/api/v1/users/me/"),
                "change_password": request.build_absolute_uri(
                    "/api/v1/auth/change-password/"
                ),
            },
        }
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    return Response({"status": "ok"})

urlpatterns = [
    path("", api_root, name="api-root"),
    path("admin/", admin.site.urls),
    path("api/v1/health/", health_check, name="health"),
    path("api/v1/", include("apps.accounts.urls")),
]
