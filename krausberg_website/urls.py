from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
# TODO
# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^services/$', views.services, name='services'),
    url(r'^service/$', views.service, name='service'),
    url(r'^job-offers/$', views.job_offer, name='job_offer'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^business/', views.business, name='business'),
    url(r'^private/', views.private, name='private'),
    url(r'^administrator/', views.administrator, name='administrator'),

    # services
    url(r'^services/1', views.service_1, name='1'),
    url(r'^services/2', views.service_2, name='2'),
    url(r'^services/3', views.service_3, name='3'),
    url(r'^services/4', views.service_4, name='4'),
    url(r'^services/5', views.service_5, name='5'),
    url(r'^services/6', views.service_6, name='6'),
    url(r'^services/7', views.service_7, name='7'),
    url(r'^services/8', views.service_8, name='8'),
    url(r'^services/9', views.service_9, name='9'),
    url(r'^services/10', views.service_10, name='10'),
    url(r'^services/11', views.service_11, name='11'),
    url(r'^services/12', views.service_12, name='12'),
    url(r'^services/13', views.service_13, name='13'),
    url(r'^services/14', views.service_14, name='14'),
    url(r'^services/15', views.service_15, name='15'),
    url(r'^services/16', views.service_16, name='16'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)