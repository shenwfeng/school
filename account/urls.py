from django.conf.urls import url
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    #url(r'login/$',views.user_login,name='user_login'),
    url(r'^login/$',auth_views.login,{'template_name':'account/login.html'},name='user_login',),
    url(r'^logout/$',auth_views.logout,name='user_logout',),
    url(r'^profile/$',views.user_profile,name='user_profile',),
    url(r'register/$',views.register,name='user_register')
]