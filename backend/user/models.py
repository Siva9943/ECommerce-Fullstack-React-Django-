from django.db import models

class User_Details(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateTimeField(auto_now_add=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15)
   
    def __str__(self):
        return self.username