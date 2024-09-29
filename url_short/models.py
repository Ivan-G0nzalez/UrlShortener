from django.db import models
from django.core.validators import MinLengthValidator

"""
class Url:
    id int
    url string
    shortcode string
    created_at datetime
    updated_at datetime
    counter int
"""

class Url(models.Model):
    url = models.CharField(max_length=255, null=False, unique=True)
    shortcode = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    counter = models.IntegerField(default=0)