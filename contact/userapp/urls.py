#django-rest imports
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from userapp.views import RegisterUser, LogoutUser




urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("logout/", LogoutUser.as_view(), name="logout")
]


