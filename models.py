from django.db import models

# Table 1: User
class User(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

# Table 2: Contact
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.phone_no}"
