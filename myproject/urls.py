"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import activate,ServiceWorkerView
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/tourist/',include('tourist.api.urls',namespace="tourist-api")),
    url(r'^api/v1/users/',include('accounts.api.urls',namespace="users-api")),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate'),#Email Activation

    url('^', include('django.contrib.auth.urls')), #email varification
    url(r'^rest-auth/', include('rest_auth.urls')), #social login
    url(r'^accounts/',include('allauth.urls'), name='socialaccount_signup'),
    url(r'^firebase-messaging-sw.js', ServiceWorkerView.as_view(), name='service_worker')# web firebase pushnotification
      
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'',TemplateView.as_view(template_name='home.html')),
]


admin.site.site_header = 'Touricted Administration'
admin.site.index_title = 'Touricted' 
admin.site.site_title = 'Touricted'