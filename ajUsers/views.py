from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import AjUsersSerializer
from .models import AjUser


class UserList(APIView):
    def get(self, request):
        user = AjUser.objects.all()
        serializer = AjUsersSerializer(user, many=True)
        return Response(serializer.data)
