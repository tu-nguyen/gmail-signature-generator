from colorfield.fields import ColorField
from colorfield.widgets import ColorWidget
from django import forms


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
    font_style_field= forms.CharField(label="Font Style", widget=forms.Select(choices=FONT_CHOICES))
    font_size_field = forms.IntegerField(label="Font Size")
    primary_color_field = forms.CharField(label="Primary Color", max_length=7, widget=forms.TextInput(attrs={'type': 'color'}))
    secondary_color_field = forms.CharField(label="Secondary Color", max_length=7, widget=forms.TextInput(attrs={'type': 'color'}))
    

class DataForm(forms.Form):
    first_name_field = forms.CharField(label="First Name", max_length=50)
    last_name_field = forms.CharField(label="Last Name", max_length=50)
    job_title_field = forms.CharField(label="Job Title", max_length=200)
    phone_number_field = forms.CharField(label="Phone Number", max_length=20)
    mobile_number_field = forms.CharField(label="Mobile Number", max_length=20)
    last_name_field = forms.CharField(label="Last Name", max_length=50)
    job_title_field = forms.CharField(label="Job Title", max_length=50)
    email_field = forms.EmailField(label="Email", max_length=50)

    website_url_field = forms.URLField(label="Website")
    linkedin_url_field = forms.URLField(label="LinkedIn")
    github_url_field = forms.URLField(label="Github")
    twitter_url_field = forms.URLField(label="Twitter")
    facebook_url_field = forms.URLField(label="Facebook")
    youtube_url_field = forms.URLField(label="Youtube")

    company_name_field = forms.CharField(label="Company Name", max_length=200)
    company_website_url_field = forms.URLField(label="Company Website")
    company_address_field = forms.CharField(label="Company Address 1", max_length=200)
    company_address_2_field = forms.CharField(label="Company Address 2", max_length=200)

    photo_url_field = forms.URLField(label="Photo URL")
    photo_link_field = forms.URLField(label="Photo Link")
    banner_url_field = forms.URLField(label="Banner URL")
    banner_link_field = forms.URLField(label="Banner Link")
