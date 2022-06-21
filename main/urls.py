"""kweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from django.conf.urls import url
from main import views

app_name = 'main'

urlpatterns = [
    url(r'^testimonial_add/$', views.TestimonialCreateView.as_view(), name='testimonial_add'),
    url(r'^testimonial_list_view/$', views.TestimonialsListView.as_view(), name='testimonial_list_view'),
    url(r'^testimonial_update/(?P<pk>\d+)/$', views.TestimonialUpdateView.as_view(), name='testimonial_update'),
    url(r'^testimonial_delete/(?P<pk>\d+)/$', views.TestimonialDeleteView.as_view(), name='testimonial_delete'),
    url(r'^client_add/$', views.ClientCreateView.as_view(), name='client_add'),
    url(r'^client_list_view/$', views.ClientListView.as_view(), name='client_list_view'),
    url(r'^client_update/(?P<pk>\d+)/$', views.ClientUpdateView.as_view(), name='client_update'),
    url(r'^client_delete/(?P<pk>\d+)/$', views.ClientDeleteView.as_view(), name='client_delete'),

]

