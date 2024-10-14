from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.api.views import UserModelViewSet, LogoutAPIView
from apps.address.api.views import AddressModelViewSet

from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register('users', UserModelViewSet, basename='users')
router.register("addresses", AddressModelViewSet, basename="addresses")


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/logout', LogoutAPIView.as_view(), name='logout'),
]

urlpatterns += router.urls
