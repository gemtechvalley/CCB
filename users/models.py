from django.db import models

from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_mobile = models.CharField(max_length=10, null=True)
    phone_home = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=10, null=True)
    nic_no = models.CharField(max_length=10, null=True)
    drl_no = models.CharField(max_length=10, null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

            

