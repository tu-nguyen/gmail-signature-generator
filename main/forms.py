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
    template_style = forms.IntegerField(label="Template Style", widget = forms.HiddenInput(), initial=1, required=False)
    font_style= forms.CharField(label="Font Style", widget=forms.Select(choices=FONT_CHOICES), required=False)
    font_size = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '3', 'id':'myRange'}),label="Font Size", min_value=1, max_value=3, initial=2, required=False)
    primary_color = forms.CharField(label="Primary Color", max_length=7, widget=forms.TextInput(attrs={'type': 'color'}))
    secondary_color = forms.CharField(label="Secondary Color", max_length=7, widget=forms.TextInput(attrs={'type': 'color'}))

class DataForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=50, required=True)), label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=50, required=True)), label="Last Name")
    job_title = forms.CharField(label="Job Title", max_length=200, required=False)
    phone_number = forms.CharField(label="Phone Number", max_length=20, required=False)
    mobile_number = forms.CharField(label="Mobile Number", max_length=20, required=False)
    job_title = forms.CharField(label="Job Title", max_length=50, required=False)
    email = forms.EmailField(label="Email", max_length=50, required=False)

    website_url = forms.URLField(label="Website", required=False)
    linkedin_url = forms.URLField(label="LinkedIn", required=False)
    github_url = forms.URLField(label="Github", required=False)
    twitter_url = forms.URLField(label="Twitter", required=False)
    facebook_url = forms.URLField(label="Facebook", required=False)
    youtube_url = forms.URLField(label="Youtube", required=False)

    company_name = forms.CharField(label="Company Name", max_length=200, required=False)
    company_website_url = forms.URLField(label="Company Website", required=False)
    company_address = forms.CharField(label="Company Address 1", max_length=200, required=False)
    company_address_2 = forms.CharField(label="Company Address 2", max_length=200, required=False)

    photo_url = forms.URLField(label="Photo URL", required=False)
    photo_link = forms.URLField(label="Photo Link", required=False)
    banner_url = forms.URLField(label="Banner URL", required=False)
    banner_link = forms.URLField(label="Banner Link", required=False)

