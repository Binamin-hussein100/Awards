from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField(default='Live in the sunshine where you belong.')
    profile_pic = CloudinaryField('image')
    
    def save(self,**kwargs):
        self.save()
        
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    def profiles_posts(self):
        self.image_set.all()
       
    def __str__(self):
        return f'{self.user.username}'
    
# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile = Profile.objects.create(user=kwargs['instance'])
# post_save.connect(create_profile, sender=User)

class Project(models.Model):
    user =  models.OneToOneField(User,null=True,on_delete=models.CASCADE,default=None,blank=True)
    title = models.CharField(max_length=30)
    landing_page = CloudinaryField('image')
    description = models.TextField() 
    link = models.URLField()
    author= models.ForeignKey(Profile, on_delete=models.CASCADE,default=None, null=True, blank=True)
    
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()