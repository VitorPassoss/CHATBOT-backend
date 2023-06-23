from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.db import transaction
from apps.authentication.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

    

class DetailsUser(APIView):
    permission_classes = [ IsAuthenticated ]
    serializer_class = UserSerializer

    def get(self, request):
        get_data = User.objects.get(pk=request.user.pk)
        user_serializer = UserSerializer(get_data).data
        data = {
            'user':user_serializer
        }
        return Response(data)
    
    def post(self, request):
        current_user = User.objects.get(pk=request.user.pk)
        email = request.data.get('email')
        password = request.data.get('password')
        current_user.username = email
        current_user.set_password(password)
        current_user.save()
        return Response({"message": "User update successfully"}, status=status.HTTP_201_CREATED)

 