from django.urls import reverse_lazy
from django.views import generic
from app_core import views
from .forms import ProfileUserCreationForm
from itertools import chain
from operator import attrgetter
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db.models import Q

#Core Handlers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, HttpResponse, render_to_response, redirect

#models
from app_users.models import ProfileUser
from app_messages.models import Message
from app_users.forms import *
from app_users.urls import *

class SignUp(generic.CreateView):
    form_class = ProfileUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'

# User Profile View
@login_required
def ProfileUserEditView(request):
    user = request.user
    profileuser = ProfileUser.objects.get(username=user.username)
    form_profile_pic = UpdateProfilePicture()
    if request.method == 'POST':
        if "change_pic" in request.POST:
            form = UpdateProfilePicture(request.POST)
            if form.is_valid():
                profileuser.profile_image = request.FILES['profile_picture']
                profileuser.save()
                return HttpResponseRedirect("profile-edit")
            else:
                print(form.errors)


        if "edit_profile" in request.POST:
            form = EditProfileUserForm(request.POST, instance=profileuser)
            if form.is_valid():
                #Save updates
                profileuser= form.save()
                form = EditProfileUserForm(instance=profileuser)
                context = {
                    'profileuser':profileuser,
                    'form_edit_profile': form,
                    'form_profile_pic': form_profile_pic,
                }
                return HttpResponseRedirect("profile-edit")
            else:
                context = {
                    'profileuser':profileuser,
                    'form_edit_profile': form,
                    'form_profile_pic': form_profile_pic,
                }
                return render(request, "userprofiles/userprofilepage.html", context)
    form = EditProfileUserForm(instance=profileuser)
    context = {
        'profileuser': profileuser,
        'form_edit_profile': form,
        'form_profile_pic': form_profile_pic,
    }
    return render(request, "userprofiles/userprofilepage.html", context)
# List of User Profiles View
@login_required
def UserProfilesListView(request):
    user = request.user
    if not ProfileUser.objects.all().filter(username=user.username).exists():
        return redirect(reverse('profile-edit'))

    profileuser = ProfileUser.objects.get(username=user.username)

    profiles = ProfileUser.objects.all().exclude(username=profileuser.username)
    #Context
    context = {
        'profiles': profiles,
        'profileuser': profileuser,
    }

    return render(request, "userprofiles/userlist.html", context)

# Messages between Users View
@login_required
def MessagesPage(request, recipient_url):
    user=request.user
    profileuser = ProfileUser.objects.get(username=user.username)
    recipient = get_object_or_404(ProfileUser, url=recipient_url)
    totalmessages = Message.objects.all().filter(Q(authorone__username=profileuser.username) | Q(authortwo__username=profileuser.username)).filter(Q(authorone__username=recipient.username) | Q(authortwo__username=recipient.username)).order_by("-created")
    numofmes = len(totalmessages)
    context = {
        'profileuser': profileuser,
        'recipient': recipient,
        'totalmessages': totalmessages,
        'numofmes': numofmes,

    }

    return render(request, "userprofiles/messages.html", context)

#Send Message
@login_required
def SendMessageView(request, recipient_url):
    user = request.user
    profileuser = get_object_or_404(ProfileUser, username=user.username)
    recipient_user = get_object_or_404(ProfileUser, url=recipient_url)
    recipient = get_object_or_404(ProfileUser, username=recipient_user.username)
    totalmessages = Message.objects.all().filter(Q(authorone__username=profileuser.username) | Q(authortwo__username=profileuser.username)).filter(Q(authorone__username=recipient.username) | Q(authortwo__username=recipient.username)).order_by("-created")
    numofmes = len(totalmessages)
    form = SendMessageForm()
    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        '''
        def clean(self):
            text = self.cleaned_data['text']
            if len(text) > 0:
                raise ValidationError('You cannot send a blank message')
            return self.cleaned_data
        '''
        if form.is_valid():
            message = form.save(commit=False)
            message.authorone = profileuser
            message.authortwo = recipient
            message.save()
            return HttpResponseRedirect(recipient_url)
        else:
            form = SendMessageForm(request.POST)

    context = {
        'profileuser': profileuser,
        'recipient': recipient,
        'form': form,
        'totalmessages':totalmessages,
        'numofmes': numofmes,

    }

    return render(request, "userprofiles/messages.html", context)

# User Profile Delete
@login_required
def ProfileUserDeleteView(request):
    """
    This view deactivates an account
    """
    user=request.user
    profileuser=ProfileUser.objects.get(username=user.username)
    form=ProfileUserDeleteForm()
    context={
        'form': form,
        'profileuser': profileuser,
    }
    if request.method == "POST":
        form = ProfileUserDeleteForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['confirm']:
                # deactivating account
                user.is_active = False
                user.save()
                logout(request)
                return redirect(reverse('index'))

    return render(request, "userprofiles/profile_delete.html", context)
