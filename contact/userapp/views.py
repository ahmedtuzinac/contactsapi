#django-rest imports 
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authtoken.models import Token
#in-apps imports
from django.contrib.auth.models import User
from userapp.serializers import RegisterUserSerializer


class RegisterUser(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class LogoutUser(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = get_object_or_404(Token,user=request.user)
        token.delete()
        return Response(status=HTTP_200_OK)






    
    

