from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ProfileUser
from django.forms import ModelForm
from app_messages.models import Message

#Create User
class ProfileUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ProfileUser
        fields = ('username','email','first_name','last_name')
    #def custom_signup(self, request, user):
    #user.save()
    # Creating user profile
    #profileuser = ProfileUser()
    #profileuser.user = user
    #profileuser.first_name = self.cleaned_data['first_name']
    #profileuser.last_name = self.cleaned_data['last_name']
    #profileuser.save()

    #return user
#Change User Details
class ProfileUserChangeForm(UserChangeForm):

    class Meta:
        model = ProfileUser
        fields = ('username','email','first_name','last_name')

# Change profile picture
class UpdateProfilePicture(forms.Form):
    profile_picture = forms.ImageField(required=False)

#Change User Profile
class EditProfileUserForm(ModelForm):

    class Meta:
        model = ProfileUser
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
#Delete User
class ProfileUserDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True)

#Send Message
#Teacher to Student Evaluation Form
class SendMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text']
