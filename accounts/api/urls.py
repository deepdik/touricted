from django.conf.urls import url

from .views import (
		UserCreateAPIView,
		UserLoginAPIView,
		ChangePasswordAPIView,
		PasswordResetView,
		FacebookLoginView,
		GoogleLoginView,
		
	)
from accounts.pushNotification.pushview import PushNotifictionAPIView


urlpatterns = [
	url(r'^register/$',UserCreateAPIView.as_view(),name="register"),
	url(r'^login/$',UserLoginAPIView.as_view(),name="login"),
	url(r'^changepassword/$',ChangePasswordAPIView.as_view(),name="changePassword"),
	url(r'^password/reset/$', PasswordResetView.as_view(),
    name='rest_password_reset'),
    url(r'^rest-auth/google/$', GoogleLoginView.as_view(), name='gl_login'), #facebooklogin
    url(r'^PushNotifiction/$',PushNotifictionAPIView.as_view(),name="pushNotifiction"),

    url(r'^rest-auth/facebook/$', FacebookLoginView.as_view(), name='fb_login'), #facebooklogin
]