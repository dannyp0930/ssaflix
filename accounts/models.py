from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit import processors
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill



class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    photo_thumbnail = ImageSpecField(
        source='photo',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 90},
    )