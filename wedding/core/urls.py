from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


app_name = 'core'
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

