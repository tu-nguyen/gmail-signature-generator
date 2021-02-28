from colorfield.fields import ColorField
from django.db import models

class MyModel(models.Model):
    color = ColorField(default='#FF0000')

# class ColorField(models.CharField):
#     def __init__(self, *args, **kwargs):
#         kwargs['max_length'] = 10
#         super(ColorField, self).__init__(*args, **kwargs)

#     def formfield(self, **kwargs):
#         kwargs['widget'] = ColorWidget
#         return super(ColorField, self).formfield(**kwargs)