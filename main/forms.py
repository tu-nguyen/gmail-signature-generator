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
    font_style_field= forms.CharField(label="Font Style", widget=forms.Select(choices=FONT_CHOICES), required=False)
    font_size_field = forms.IntegerField(label="Font Size", min_value=1, max_value=3, required=False)
    primary_color_field = forms.CharField(label="Primary Color", max_length=7, widget=forms.TextInput(attrs={'type': 'color'}))
    secondary_color_field = forms.CharField(label="Secondary Color", max_length=7, widget=forms.TextInput(attrs={'type': 'color'}))

class DataForm(forms.Form):
    # first_name_field = forms.CharField(label="First Name", max_length=50, required=True)
    # last_name_field = forms.CharField(label="Last Name", max_length=50, required=True)
    first_name_field = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=50, required=True)), label="First Name")
    last_name_field = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=50, required=True)), label="Last Name")
    job_title_field = forms.CharField(label="Job Title", max_length=200, required=False)
    phone_number_field = forms.CharField(label="Phone Number", max_length=20, required=False)
    mobile_number_field = forms.CharField(label="Mobile Number", max_length=20, required=False)
    job_title_field = forms.CharField(label="Job Title", max_length=50, required=False)
    email_field = forms.EmailField(label="Email", max_length=50, required=False)

    website_url_field = forms.URLField(label="Website", required=False)
    linkedin_url_field = forms.URLField(label="LinkedIn", required=False)
    github_url_field = forms.URLField(label="Github", required=False)
    twitter_url_field = forms.URLField(label="Twitter", required=False)
    facebook_url_field = forms.URLField(label="Facebook", required=False)
    youtube_url_field = forms.URLField(label="Youtube", required=False)

    company_name_field = forms.CharField(label="Company Name", max_length=200, required=False)
    company_website_url_field = forms.URLField(label="Company Website", required=False)
    company_address_field = forms.CharField(label="Company Address 1", max_length=200, required=False)
    company_address_2_field = forms.CharField(label="Company Address 2", max_length=200, required=False)

    photo_url_field = forms.URLField(label="Photo URL", required=False)
    photo_link_field = forms.URLField(label="Photo Link", required=False)
    banner_url_field = forms.URLField(label="Banner URL", required=False)
    banner_link_field = forms.URLField(label="Banner Link", required=False)

