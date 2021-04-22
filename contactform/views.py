from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from data.models import Data
from django.contrib.auth import authenticate, login, logout
import datetime

# Create your views here.

def contact_add(request):

	now = datetime.datetime.now()
	year = now.year
	month = now.month
	day = now.day

	if len(str(day)) == 1:
		day = "0" + str(day)

	if len(str(month)) == 1:
		month = "0" + str(month)

	today = str(day) + "/" + str(month) + "/" + str(year)
	time = str(now.hour) + ":" + str(now.minute)


	if request.method == "POST":

		name = request.POST.get('name')
		email = request.POST.get('email')
		subj = request.POST.get('subj')
		msg = request.POST.get('msg')

		if name == "" or email == "" or subj == "" or msg == "":
			txt = "All Fields Required!"
			goback = "/contact"
			return render(request, 'front/msgbox.html', {'txt': txt, 'goback': goback})

		b = ContactForm(name=name, email=email, subj=subj, msg=msg, date=today, time=time)
		b.save()
		txt = "Your Message Received!"
		goback = "/contact"
		return render(request, 'front/msgbox.html', {'txt': txt, 'goback': goback})


	return render(request, 'front/msgbox.html')

def contact_show(request):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	txt = ContactForm.objects.all()

	return render(request, 'back/contact_form.html', {'txt': txt})

def contact_delete(request, pk):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	b = ContactForm.objects.filter(pk=pk)
	b.delete()
	return redirect('contact_show')