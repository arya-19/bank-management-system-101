from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from data.models import Data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission

# Create your views here.

def manager_list(request):

	manager = Manager.objects.all()

	return render(request, 'back/manager_list.html', {'manager': manager})

def manager_delete(request, pk):

	manager = Manager.objects.get(pk=pk)
	b = User.objects.filter(username=manager.uuser)
	b.delete()
	manager.delete()

	return redirect('manager_list')

def manager_group(request):

	group = Group.objects.all()	

	return render(request, 'back/manager_group.html', {'group': group})

def manager_group_add(request):

	if request.method == "POST":

		name = request.POST.get('name')

		if name != "":

			if len(Group.objects.filter(name=name)) == 0:

				group = Group(name=name)
				group.save()

	return redirect('manager_group')

def manager_group_delete(request, name):

	b = Group.objects.filter(name=name)
	b.delete()

	return redirect('manager_group')

