from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE,default=None,blank=True)
    bio = models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')
    
    def __str__(self):
        return f'{self.user.username}'
    
    def save(self):
        super().save()
        
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    def profiles_posts(self):
        self.image_set.all()
        
    def user_profile(sender,**kwargs):
        if kwargs['created']:
            prof = Profile.objects.create(user=kwargs['instance'])

    post_save.connect(user_profile, sender=User)