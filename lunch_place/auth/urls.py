from django.urls import path
from auth.views import LoginView, EmployeeRegisterView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', EmployeeRegisterView.as_view(), name='auth_register'),
]
