from rest_framework.generics import (
		CreateAPIView,
	)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_400_BAD_REQUEST
	,HTTP_204_NO_CONTENT
	)
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import (
		UserCreateSerializer,
		UserLoginSerializer,
		ChangePasswordSerializer,
	)
from .permissions import IsAuthenticatedOrCreate

User = get_user_model()

#PASSWORD RESET BY EMAIL START------

from .settings import (  
    PasswordResetSerializer,     
)
from rest_framework.generics import GenericAPIView
from rest_framework import status

#END--------------------------------
#SOCIAL LOGIN START-----------------

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

#END-------------------------------

from rest_framework_jwt.authentication import  JSONWebTokenAuthentication
class UserCreateAPIView(CreateAPIView):
	querset = User.objects.all()
	serializer_class = UserCreateSerializer
	permission_classes = (IsAuthenticatedOrCreate,)
	


class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer
	authentication_classes = [JSONWebTokenAuthentication]
	
	def post(self,request,*args,**kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data,status=HTTP_200_OK)
		return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class ChangePasswordAPIView(APIView):
	permission_classes = (IsAuthenticated,)
	authentication_classes = [JSONWebTokenAuthentication]

	def get_object(self):
		return self.request.user

	def put(self,request,*args,**kwargs):
		user = self.get_object()
		serializer = ChangePasswordSerializer(data=request.data)
		if serializer.is_valid():
			oldPassword = serializer.data.get("oldPassword")
			newPassword = serializer.data.get("newPassword")
			if not user.check_password(oldPassword):
				return Response({"oldPassword":["You entered wrong password"]},
					status=HTTP_400_BAD_REQUEST)
			user.set_password(newPassword)
			user.save()
			return Response(status=HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class PasswordResetView(GenericAPIView):
    """
    Calls Django Auth PasswordResetForm save method.
    Accepts the following POST parameters: email
    Returns the success/fail message.
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return Response(
            {"success": "Password reset e-mail has been sent."},
            status=status.HTTP_200_OK
        )

class FacebookLoginView(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    authentication_classes = [JSONWebTokenAuthentication]


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    authentication_classes = [JSONWebTokenAuthentication]





