from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from accounts.email.main import SendEmail
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django import forms
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.utils.translation import gettext, gettext_lazy as _

UserModel = get_user_model()


class MyPasswordResetForm(forms.Form):
	email = forms.EmailField(label=_("Email"), max_length=254)

	def send_mail(self, subject_template_name, email_template_name,
				  context, from_email, to_email, html_email_template_name=None):
		"""
		Send a django.core.mail.EmailMultiAlternatives to `to_email`.
		"""
		subject = loader.render_to_string(subject_template_name, context)		
		# Email subject *must not* contain newlines
		subject = ''.join(subject.splitlines())		
		message = loader.render_to_string(email_template_name, context)

		SendEmail.send_email_varification_mail(to_email,subject,message)

		
	def get_users(self, email):
		"""Given an email, return matching user(s) who should receive a reset.
		This allows subclasses to more easily customize the default policies
		that prevent inactive users and users with unusable passwords from
		resetting their password.
		"""
		active_users = UserModel._default_manager.filter(**{
			'%s__iexact' % UserModel.get_email_field_name(): email,
			'is_active': True,
		})
		return (u for u in active_users if u.has_usable_password())

	def save(self, domain_override=None,
			 subject_template_name='registration/password_reset_subject.txt',
			 email_template_name='registration/password_reset_email.html',
			 use_https=False, token_generator=default_token_generator,
			 from_email=None, request=None, html_email_template_name=None,
			 extra_email_context=None):
		"""
		Generate a one-use only link for resetting password and send it to the
		user.
		"""
		email = self.cleaned_data["email"]
		for user in self.get_users(email):
			if not domain_override:
				current_site = get_current_site(request)
				site_name = current_site.name
				domain = current_site.domain
			else:
				site_name = domain = domain_override
			context = {
				'email': email,
				'domain': domain,
				'site_name': site_name,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'user': user,
				'token': token_generator.make_token(user),
				'protocol': 'https' if use_https else 'http',
				**(extra_email_context or {}),
			}
			self.send_mail(
				subject_template_name, email_template_name, context, from_email,
				email, html_email_template_name=html_email_template_name,
			)




