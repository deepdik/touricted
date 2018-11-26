from fcm_django.models import FCMDevice
from rest_framework.views import APIView
from rest_framework.response import Response

class PushNotifictionAPIView(APIView):
	def get(self, request, format=None):

		device = FCMDevice.objects.all().first()
		print(device)

		device.send_message("Title", "Message")
		device.send_message(data={"test": "test"})
		device.send_message(title="Title", body="Message", data={"test": "test"})
		return Response('success')