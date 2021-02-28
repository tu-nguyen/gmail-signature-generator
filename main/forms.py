from django import forms
from colorfield.fields import ColorField

FONT_CHOICES= [
    ('arial', 'Arial'),
    ('comic_sans_ms', 'Comic Sans MS'),
    ('courier', 'Courier'),
    ('roboto', 'Roboto'),
    ('tahoma', 'Tahoma'),
    ('time_new_roman', 'Times New Roman'),
    ('trebuchet', 'Trebuchet MS'),
    ('lucida_console', 'Lucida Console'),
    ('verdana', 'Verdana'),
    ]

class StyleForm(forms.Form):
    font_style_field= forms.CharField(label="Font Style", widget=forms.Select(choices=FRUIT_CHOICES))
    font_size_field = forms.IntegerField(label="Font Size")
    primary_color_field = forms.CharField(label="Primary Color", widget=ColorPickerWidget)
    secondary_color_field = forms.CharField(label="Secondary Color", widget=ColorPickerWidget)
    

class DataForm(forms.Form):
    first_name_field = forms.CharField(label="First Name", max_length=200)
    last_name_field = forms.CharField(label="Last Name", max_length=200)
    job_title_field = forms.CharField(label="Job Title", max_length=200)


    # //phone
    # //mobile
    # //email

    # //linkedin
    # //twitter
    # //facebook
    # //instagram
    # //youtube

    # //company name
    # //company website
    # //company address
    # //company address 2


    # //photo_url
    # //photo_link
    # //banner_url
    # //banner_link