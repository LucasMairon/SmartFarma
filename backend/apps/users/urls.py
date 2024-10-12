from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api.views import UserModelViewSet, LogoutAPIView

from rest_framework.routers import SimpleRouter

user_router = SimpleRouter()
user_router.register('api/users', UserModelViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout', LogoutAPIView.as_view(), name='logout'),
]

urlpatterns += user_router.urls
