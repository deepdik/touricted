from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token
# Create your views here.


User = get_user_model()

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		success_html="""
			<!DOCTYPE html>
		<html lang="en">
		<head>
  		<meta charset="UTF-8">
  		<title>Success</title>
		</head>
		<body>
  			<h1>Your account is activated successfully</h1>
		</body>
		</html>"""
		invalid_token_html="""
			<!DOCTYPE html>
		<html lang="en">
		<head>
  		<meta charset="UTF-8">
  		<title>Success</title>
		</head>
		<body>
  			<h1>Invalid token</h1>
		</body>
		</html>"""

		return HttpResponse(success_html)
	else:
		return HttpResponse(invalid_token_html)