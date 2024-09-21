from django.urls import path
from account.api.views import AuthView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='user-auth')
]