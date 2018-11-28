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
  
  console.log(JSON.parse(payload.data.notification))
  const data = JSON.parse(payload.data.notification)

  // Customize notification here
  const notificationTitle = data.title;
  const notificationOption = {
    body: data.body,
    icon: data.icon
    
  };

  return self.registration.showNotification(notificationTitle,
      notificationOptions);
});

