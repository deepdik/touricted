importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.
firebase.initializeApp({
  'messagingSenderId': '520542740498'
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  // Customize notification here
  const notificationTitle = 'Background Message Title';
  const notificationOptions = {
    body: 'Background Message body.',
    icon: '/itwonders-web-logo.png'
  };

  return self.registration.showNotification(notificationTitle,
      notificationOptions);
});

 curl -X POST -H "Authorization: key=AAAAeTLD4BI:APA91bGVco5pxb1iy0Z0hQxrJNKRPy1xYW3sBYa6ZK9d6o2qjAPPcW_tg1cuNZ5kQiFNvx4nS1F7Ix1r_aR_wxItXQFXDC2CQZYSKKFuR0NfWpJmTCt1Kz38DVqYtfXIz9j8G8ACPD2C" -H "Content-Type: application/json"    -d '{
  "data": {
    "notifications": {
        "title": "FCM Message",
        "body": "This is an FCM Message",
        "icon": "http://localhost:8000/media/CatImg/Screenshot_from_2018-08-21_02-19-12.png",
    }
  },
  "to": "fWYqQXpzcNE:APA91bFDJHnjF1BezFwGM91hjW26ZWU3M5XgZFyBOC14lgRC4u7-GRfT7lqEho7XLdw7dvm5sklU1kmjFU5bfuP22ROSUMrXE7b8lOfQhwHq4IQmp6oW1qc2lYmi-95xoHTOLglw2fWw"

}' https://fcm.googleapis.com/fcm/send

curl -X POST -H "Authorization: key=<Server Key>" -H "Content-Type: application/json" \
   -d '{
  "data": {
    "notifications": {
        "title": "FCM Message",
        "body": "This is an FCM Message",
        "icon": "http://localhost:8000/media/CatImg/Screenshot_from_2018-08-21_02-19-12.png",
    }
  },
  "to": "fWYqQXpzcNE:APA91bFDJHnjF1BezFwGM91hjW26ZWU3M5XgZFyBOC14lgRC4u7-GRfT7lqEho7XLdw7dvm5sklU1kmjFU5bfuP22ROSUMrXE7b8lOfQhwHq4IQmp6oW1qc2lYmi-95xoHTOLglw2fWw"
}' https://fcm.googleapis.com/fcm/send