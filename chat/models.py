import email
from xmlrpc.client import _datetime_type
from django.db import models

# Create your models here.

class customer(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null= True)
    date_created = models.DateField(auto_now_add = True, null=True)

    def __str__(self) -> str:
        return "{}      {}      {}     {}".format(self.id, self.name, self.email, self.date_created)


class messages_channel(models.Model):
    id = models.AutoField(primary_key = True)
    id_sender = models.IntegerField(null = True)
    id_recipient = models.IntegerField(null = True)
    date_created = models.DateField(auto_now_add = True, null=True)

    def __str__(self) -> str:
        return "{}      {}      {}     {}".format(self.id, self.id_sender, self.id_recipient, self.date_created)


class messages(models.Model):
    id = models.AutoField(primary_key = True)
    id_messages_channel = models.IntegerField(null = True)
    data = models.CharField(max_length=1000, null = True)
    date_created = models.DateField(auto_now_add = True, null=True)

    def __str__(self) -> str:
        return "{}      {}      {}     {}".format(self.id, self.id_messages_channel, self.data, self.date_created)


# class group_member(models.Model):
#     id = models.AutoField(primary_key = True)

#     id__channel = models.IntegerField(null = True)

#     id_messages_channel = models.IntegerField(null = True)
    
#     date_joined = models.DateField(auto_now_add = True, null=True)
#     date_left = models.DateField(null=True)

#     def __str__(self) -> str:
#         return "{}      {}".format(self.id, self.date_created, self.date_created)