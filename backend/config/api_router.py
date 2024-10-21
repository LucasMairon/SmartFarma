from django.urls import path
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.users.api.views import UserModelViewSet, LogoutAPIView
from apps.cart.api.views import CartGenericAPIView
from apps.product.api.views import ProductModelViewSet
from apps.order_item.api.views import OrderItemModelViewSet
from apps.purchase.api.views import PurchaseModelViewSet

from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register('users', UserModelViewSet, basename='users')
router.register("cart", CartGenericAPIView, basename="cart")
router.register("products", ProductModelViewSet, basename="products")
router.register("order_item", OrderItemModelViewSet, basename="order_item")
router.register("purchase", PurchaseModelViewSet, basename="purchase")


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('users/logout', LogoutAPIView.as_view(), name='logout'),
]

urlpatterns += router.urls
