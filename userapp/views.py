from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid
from django_filters.rest_framework import DjangoFilterBackend

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'is_active']
        
    def get_queryset(self):
        return User.objects.all()
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer