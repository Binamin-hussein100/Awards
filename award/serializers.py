from django.db.models import fields
from rest_framework import serializers
from .models import Project

# add code here
class ProjectSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ('user','title','description','landing_page','link')