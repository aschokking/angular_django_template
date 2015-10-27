from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

from django.views.generic import TemplateView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="base.html"), name='app'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
