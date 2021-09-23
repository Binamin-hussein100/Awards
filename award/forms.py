from django import forms
from django.forms import fields, widgets
from .models import Project,Profile

# your code here
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title','landing_page','description','link']



class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']