from django import forms
from django.forms import widgets
from .models import Project,Profile

# your code here
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['title','landing_page','description','link']
