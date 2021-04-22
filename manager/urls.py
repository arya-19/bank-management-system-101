from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^panel/manager/list/$', views.manager_list, name='manager_list'),
	url(r'^panel/manager/delete(?P<pk>\d+)/$', views.manager_delete, name='manager_delete'),
	url(r'^panel/manager/group/$', views.manager_group, name='manager_group'),
	url(r'^panel/manager/group/add/$', views.manager_group_add, name='manager_group_add'),
	url(r'^panel/manager/group/delete(?P<name>.*)/$', views.manager_group_delete, name='manager_group_delete'),

]