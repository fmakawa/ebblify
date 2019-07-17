from django.urls import path
from app_users import views
from django.conf.urls import url

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile-edit', views.ProfileUserEditView, name='profile-edit'),
    path('profileusers-list', views.UserProfilesListView, name='profileuser-list'),
    url(r'^(?P<recipient_url>[\w-]+)$', views.SendMessageView, name='send-message'),
    url(r'^(?P<recipient_url>[\w-]+)$', views.MessagesPage, name='messages-page'),
    path('profile-delete', views.ProfileUserDeleteView, name='profile-delete'),
]
