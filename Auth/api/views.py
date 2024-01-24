from rest_framework.response import Response
from rest_framework.views import APIView
from .serialize import UserRegisterSerializer
from rest_framework import status

class SignUpView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        content = {"message": "Accoutn created successfully!"}
        return Response(content)