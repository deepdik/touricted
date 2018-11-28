from fcm_django.models import FCMDevice
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import requests
import json

class PushNotifictionAPIView(APIView):
	def get(self, request, format=None):

		headers = {"Content-type": "application/json",
		            "Authorization": "key=AAAAeTLD4BI:APA91bGVco5pxb1iy0Z0hQxrJNKRPy1xYW3sBYa6ZK9d6o2qjAPPcW_tg1cuNZ5kQiFNvx4nS1F7Ix1r_aR_wxItXQFXDC2CQZYSKKFuR0NfWpJmTCt1Kz38DVqYtfXIz9j8G8ACPD2C"}
		url ="https://fcm.googleapis.com/fcm/send"
		data={
		  "to": "fWYqQXpzcNE:APA91bFDJHnjF1BezFwGM91hjW26ZWU3M5XgZFyBOC14lgRC4u7-GRfT7lqEho7XLdw7dvm5sklU1kmjFU5bfuP22ROSUMrXE7b8lOfQhwHq4IQmp6oW1qc2lYmi-95xoHTOLglw2fWw",
		  "notification": {
		    "title": "success",
		    "body":"hello ",
		    "icon": "https://www.google.co.in/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjWqo2akffeAhUREnIKHQIZDpcQjRx6BAgBEAU&url=http%3A%2F%2Fchittagongit.com%2Ficon%2Fnotification-icon-24.html&psig=AOvVaw0N5FvMLQN_a9jn54QzDQMC&ust=1543496064015457",
		    "badge": "https://www.google.co.in/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjWqo2akffeAhUREnIKHQIZDpcQjRx6BAgBEAU&url=http%3A%2F%2Fchittagongit.com%2Ficon%2Fnotification-icon-24.html&psig=AOvVaw0N5FvMLQN_a9jn54QzDQMC&ust=1543496064015457"
		  }
		}
		r = requests.post(url,data=json.dumps(data),headers=headers )

		
		return Response("success")



