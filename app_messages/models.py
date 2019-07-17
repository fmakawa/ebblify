from django.db import models
from ebblify import settings
from app_users.models import *


#General Message Model
class Message(models.Model):
    #Created
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Creation Date')
    #Author
    authorone = models.ForeignKey(ProfileUser,verbose_name='Author One',blank = False, null = False,related_name='user_first_profile',on_delete=models.CASCADE)
    authortwo = models.ForeignKey(ProfileUser, verbose_name='Author Two',blank = False, null = False,related_name='user_second_profile',on_delete=models.CASCADE)
    #Message Text
    text = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Text')
    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Message'

    def __unicode__(self):
        if self.authorone:
            return "%s" % self.authorone
        elif self.authortwo:
            return "%s" % self.authortwo
        else:
            return "%s" % self.id
