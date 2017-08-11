from rest_framework import serializers
from .models import AjUser


class AjUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AjUser
        # below line will return only the selected items username and password
        # fields = ('userName', 'password', 'gender', 'emailId', 'phoneNumber')

        # below line will return all the data in model
        fields = '__all__'
