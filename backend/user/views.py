from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User_Details
from rest_framework import status
from django.contrib.auth import authenticate


class SignupUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user_data=serializer.data
            User_Details.objects.create(
                username=user_data['username'],
                email=user_data['email'],
                address=user_data['address'],
                phone_number=user_data['phone_number']
            )

            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"error": "Email and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(username=email, password=password)

        if user is not None:
            return Response({
                "message": "Login success",
                "user": {
                    "username": user.username,
                    "email": user.email
                }
            }, status=status.HTTP_200_OK)

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )