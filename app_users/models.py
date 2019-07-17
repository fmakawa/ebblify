from django.db import models
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser
from django.shortcuts import redirect
from ebblify import settings


#UserImages Folder
def user_avatar_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/avatar/username/<filename>
    return 'users/avatar/{0}/{1}'.format(instance.username.replace(" ", "_").lower(), filename)
#User Profile
class ProfileUser(AbstractUser):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)#,blank=True, null=False)
    username = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Username', unique=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Creation Date')
    email = models.EmailField(max_length=254, blank=True, null=True)
    password = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Password')
    first_name = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Last Name')
    profile_image = models.ImageField(upload_to=user_avatar_directory_path, blank = True, null = True, default='/perfil.png')
    url = models.SlugField(max_length=400, null=True, blank = True, verbose_name='Url')

    class Meta:
        verbose_name_plural = 'UserProfile'
        verbose_name = 'UserProfiles'

    def __unicode__(self):
        return "%s" % (self.user.email)
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        url =  str(self.first_name).lower() + '_' + str(self.last_name).lower()
        self.url = url
        try:
            this = ProfileUser.objects.get(id=self.id)
            if this.profile_image != self.profile_image:
                this.profile_image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case

        super(ProfileUser, self).save(*args, **kwargs)
"""
@receiver(post_save, sender=User)
def update_user_profile (sender, instance, created, **kwargs):
    if created:
        ProfileUser.objects.create(user=instance)
    instance.ProfileUser.save()
"""
