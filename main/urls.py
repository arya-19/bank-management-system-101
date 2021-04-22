from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^services/$', views.services, name='services'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^panel/$', views.panel, name='panel'),
	url(r'^login/$', views.mylogin, name='mylogin'),
	url(r'^logout/$', views.mylogout, name='mylogout'),
	url(r'^panel/change/pass/$', views.change_pass, name='change_pass'),
	url(r'^answer/comments(?P<pk>\d+)/$', views.answer_cm, name='answer_cm'),

]
