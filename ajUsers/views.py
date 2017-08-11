from django.contrib.sites import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import AjUsersSerializer
from .models import AjUser


class UserList(APIView):
    def get(self, request):
        """This function will return the list of all users"""
        user = AjUser.objects.all()
        if user:
            serializer = AjUsersSerializer(user, many=True)
            data = ({'status': 'success', 'result': serializer.data})
            return Response(data)
        else:
            content = {'message': 'No data found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


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
                content = {'status': 'failed', 'message': 'No data found'}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = AjUsersSerializer(queryset, many=True)
                data = ({'status': 'success', 'result': serializer.data})
            return Response(data)
        else:
            content = {'status': 'failed', 'message': 'Bad request. Wrong parameters'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """ This method will help to create a new user
            @:param username
            @:param password
            @:param gender
            @:param emailId
            @:param phoneNumber
            """
        username = request.GET.get('userName', None)
        password = request.GET.get('password', None)
        gender = request.GET.get('gender', None)
        emailid = request.GET.get('emailId', None)
        phonenumber = request.GET.get('phoneNumber', None)

        if phonenumber:
            user = AjUser.objects.all()
            queryset = user.filter(phoneNumber=phonenumber)
            if queryset:
                content = {'status': 'failed', 'message': 'User exists with this phonenumber'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if username and password and gender and emailid and phonenumber:
            ajuser = AjUser()
            ajuser.userName = username
            ajuser.password = password
            ajuser.gender = gender
            ajuser.emailId = emailid
            ajuser.phoneNumber = phonenumber

            try:
                isCreated = ajuser.save()
                user = AjUser.objects.all()
                queryset = user.filter(phoneNumber=phonenumber)
                serializer = AjUsersSerializer(queryset, many=True)
                content = {'status': 'success', 'message': 'Create New user',
                           'result': serializer.data}
                return Response(content, status=status.HTTP_201_CREATED)
            except (not isCreated):
                content = {'status': 'failed', 'message': 'Server Error'}
                return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            content = {'status': 'failed', 'message': 'Bad request. Wrong parameters'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

