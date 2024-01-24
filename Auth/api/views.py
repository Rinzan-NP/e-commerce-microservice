from rest_framework.response import Response
from rest_framework.views import APIView
from .serialize import UserRegisterSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed,ParseError
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class SignUpView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        content = {"message": "Accoutn created successfully!"}
        return Response(content)

class LoginView(APIView):
    def post(self, request):
        try:
            email = request.data["email"]
            password = request.data["password"]

        except KeyError:
            raise ParseError("All Fields Are Required")

        if not User.objects.filter(email=email).exists():
            raise AuthenticationFailed("Invalid Email Address")

        if not User.objects.filter(email=email, is_active=True).exists():
            raise AuthenticationFailed(
                "You are blocked by admin ! Please contact admin"
            )

        user = authenticate(username=email, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid Password")

        refresh = RefreshToken.for_user(user)
        refresh["first_name"] = str(user.first_name)
        refresh["is_superuser"] = user.is_superuser
        content = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "isAdmin": user.is_superuser,
        }

        return Response(content, status=status.HTTP_200_OK)