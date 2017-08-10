from django.http import Http404
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializer import AjUsersSerializer
from .models import AjUser


class UserList(APIView):
    def get(self, request):
        user = AjUser.objects.all()
        serializer = AjUsersSerializer(user, many=True)
        data = ({'status': 'success', 'result': serializer.data})
        return Response(data)


class FetchAjUser(APIView):
    def get(self, request):
        userName = request.GET.get('userName')

        if userName is not None:
            user = AjUser.objects.all()
            queryset = user.filter(userName=userName)
            serializer = AjUsersSerializer(queryset, many=True)
            data = ({'status': 'success', 'result': serializer.data})
            return Response(data)
        else:
            raise Http404("No user found")
