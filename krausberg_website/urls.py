from django.conf.urls import include, url
from django.contrib import admin
from . import views

# TODO
# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^services/$', views.services, name='services'),
    url(r'^service/$', views.service, name='service'),
    url(r'^job-offers/$', views.job_offer, name='job_offer'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^business/', views.business, name='business'),
]