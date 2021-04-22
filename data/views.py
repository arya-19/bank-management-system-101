from django.shortcuts import render, get_object_or_404, redirect
from .models import Data
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def data_list(request):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	data = Data.objects.all()

	return render(request, 'back/data_list.html', {'data': data})

def data_add(request):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	if request.method == "POST":
		
		name = request.POST.get("name")
		about = request.POST.get("about")
		fill = request.POST.get("fill")
		icon = request.POST.get("icon")

		if name == "" or about == "" or fill == "" or icon == "":
			error = "All Fields Required!"
			return render(request, 'back/error.html', {'error': error})

		b = Data(name=name, about=about, fill=fill, icon=icon)
		b.save()
		return redirect('data_list')

	return render(request, 'back/data_add.html')

def data_delete(request, pk):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	b = Data.objects.filter(pk=pk)
	b.delete()
	return redirect('data_list')

def data_edit(request, pk):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	if len(Data.objects.filter(pk=pk)) == 0:

		error = "Data Not Found!"
		return render(request, 'back/error.html', {'error': error})

	data = Data.objects.get(pk=pk)

	if request.method == "POST":

		name = request.POST.get("name")
		about = request.POST.get("about")
		fill = request.POST.get("fill")
		icon = request.POST.get("icon")

		if name == "" or about == "" or fill == "" or icon == "":
			error = "All Fields Required!"
			return render(request, 'back/error.html', {'error': error})

			
		b = Data.objects.get(pk=pk)
		b.name = name
		b.about = about
		b.fill = fill
		b.icon = icon
		b.save()

		return redirect('data_list')

	return render(request, 'back/data_edit.html', {'pk': pk, 'data': data})
