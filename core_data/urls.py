from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^tyquy/', include('tyquy.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


