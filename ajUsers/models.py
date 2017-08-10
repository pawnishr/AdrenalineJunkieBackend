from django.db import models


class AjUser(models.Model):
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    emailId = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=20)

    # helps print a value on search of object. Help to show the specific details from object on search from
    def __str__(self):
        return self.userName + ' - ' + self.gender
