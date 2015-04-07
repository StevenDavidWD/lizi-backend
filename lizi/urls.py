from django.conf.urls import patterns, url

from lizi import views

urlpatterns = patterns('',
    url(r'^login/', views.login, name='login'),
    url(r'^reg/', views.reg, name='reg'),
    url(r'^test/', views.test, name='test'),
    url(r'^refresh/', views.refresh, name='refresh')
)
