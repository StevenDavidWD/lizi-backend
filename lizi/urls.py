from django.conf.urls import patterns, url

from lizi import views

urlpatterns = patterns('',
    url(r'^login/', views.login, name='login'),
    url(r'^reg/', views.reg, name='reg'),
)
