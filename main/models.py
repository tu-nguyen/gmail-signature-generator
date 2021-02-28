from colorfield.fields import ColorField
from django.db import models

class MyModel(model.Model):
    color = ColorField(default='#FF0000')