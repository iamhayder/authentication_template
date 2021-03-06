from django.urls import path, include
from .views import ListUsers

app_name = "authentication"

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/register/', include('dj_rest_auth.registration.urls')),
    path('listusers/', ListUsers.as_view())
]
