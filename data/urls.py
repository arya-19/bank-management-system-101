from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^panel/data/list', views.data_list, name='data_list'),
	url(r'^panel/data/add', views.data_add, name='data_add'),
	url(r'^panel/data/delete(?P<pk>\d+)/$', views.data_delete, name='data_delete'),
	url(r'^panel/data/edit(?P<pk>\d+)/$', views.data_edit, name='data_edit'),

]