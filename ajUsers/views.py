from django.http import Http404, HttpResponseServerError
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
        """ This method will help to fetch all users details
            @:param username
            @:param phonenumber
        """
        username = request.GET.get('userName')
        phonenumber = request.GET.get('phoneNumber')

        if username is not None:
            user = AjUser.objects.all()
            queryset = user.filter(userName=username, phoneNumber=phonenumber)
            if not queryset:
                raise Http404()
            else:
                serializer = AjUsersSerializer(queryset, many=True)
                data = ({'status': 'success', 'result': serializer.data})
            return Response(data)
        else:
            raise Http404()

    def put(self, request):
        """ This method will help to create a new user """
        username = request.GET.get('userName', None)
        password = request.GET.get('password', None)
        gender = request.GET.get('gender', None)
        emailid = request.GET.get('emailId', None)
        phonenumber = request.GET.get('phoneNumber', None)

        if username and password and gender and emailid and phonenumber:
            ajuser = AjUser()
            ajuser.userName = username
            ajuser.password = password
            ajuser.gender = gender
            ajuser.emailId = emailid
            ajuser.phoneNumber = phonenumber
            ajuser.save()
            isCreated = ajuser.save()
            if isCreated:
                data = ({'status': 'success'})
                return HttpResponse(data)
            else:
                return HttpResponseServerError()
                raise HttpResponse(status=500)
        else:
            raise Http404
