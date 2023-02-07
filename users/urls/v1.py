from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView

from users import views


urlpatterns = [
    path('users/', views.UserViewSet.as_view({'post': 'create_user'})),
    path('users/token/', views.UserViewSet.as_view({'post': 'create_token'})),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
