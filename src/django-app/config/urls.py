from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import CustomTokenObtainPairView

router = routers.DefaultRouter()

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path(
        "auth/jwt/create/",
        CustomTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("accounts/", include("accounts.urls")),
    path("shops/", include("shops.urls")),
    path("quotes/", include("quotes.urls")),
    path("misc/", include("misc.urls")),
    path("vehicles/", include("vehicles.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redocs/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
