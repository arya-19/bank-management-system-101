from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from data.models import Data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from manager.models import Manager

# Create your views here.

def home(request):

	site = Main.objects.get(pk=1)

	request.session['test'] = "hello"

	print(request.session['test'])

	return render(request, 'front/home.html', {'site': site})

def about(request):

	site = Main.objects.get(pk=1)

	return render(request, 'front/about.html', {'site': site})

def services(request):

	site = Main.objects.get(pk=1)
	data = Data.objects.all()

	return render(request, 'front/services.html', {'site': site, 'data': data})

def contact(request):

	site = Main.objects.get(pk=1)

	return render(request, 'front/contact.html', {'site': site})

def panel(request):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	return render(request, 'back/home.html')

def mylogin(request):

	if request.method == "POST":

		uuser = request.POST.get("username")
		upass = request.POST.get("password")

		if uuser != "" and upass != "":

			user = authenticate(username = uuser, password = upass)

			if user != None:

				login(request, user)
				return redirect('panel')


	return render(request, 'front/login.html')

def mylogout(request):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	logout(request)

	return redirect('mylogin')

def change_pass(request):

	#login check starts

	if not request.user.is_authenticated:
		return redirect('mylogin')

	#login check ends

	if request.method == "POST":

		oldpass = request.POST.get('oldpass')
		newpass = request.POST.get('newpass')
		cnewpass = request.POST.get('cnewpass')

		if oldpass == "" or newpass == "" or cnewpass == "":

			error = "All Fields Required!"
			return render(request, 'back/error.html', {'error': error})

		user = authenticate(username = request.user, password = oldpass)

		if user != None:
			
			if len(newpass) < 8:

				error = "Your Password Must Be At Least 8 Characters!"
				return render(request, 'back/error.html', {'error': error})

			if oldpass == newpass:

				error = "New Password And Old Password Cannot Be Same!"
				return render(request, 'back/error.html', {'error': error})
			
			if newpass != cnewpass:

				error = "The passwords don't match!"
				return render(request, 'back/error.html', {'error': error})	

			c1 = 0
			c2 = 0
			c3 = 0
			c4 = 0

			for c in newpass:
				if c >= "0" and c <= "9":
					c1 = 1
			for c in newpass:
				if c >= "A" and c <= "Z":
					c2 = 1
			for c in newpass:
				if c >= "a" and c <= "z":
					c3 = 1
			for c in newpass:
				if c in '~!@#$%^&*()_+=-`':
					c4 = 1

			if c1 == 0 or c2 == 0 or c3 == 0 or c4 == 0:		

				error = "The New Password should have at least 1 Capital Letter, 1 Small Letter, 1 Number and 1 Character!"
				return render(request, 'back/error.html', {'error': error})	

			user = User.objects.get(username = request.user)		
			user.set_password(cnewpass)
			user.save()
			return redirect('mylogout')
		
		else:

			error = "Your Password Is Not Correct!"
			return render(request, 'back/error.html', {'error': error})


	return render(request, 'back/changepass.html')

def myregister(request):

	if request.method == "POST":

		uuser = request.POST.get("username")
		uemail = request.POST.get("email")
		upass = request.POST.get("pass")
		ucpass = request.POST.get("cpass")

		if uuser != "" and uemail != "" and upass != "" and ucpass != "":

			if upass != ucpass:

				txt = "The passwords don't match!"
				goback = "/register"
				return render(request, 'front/msgbox.html', {'txt': txt, 'goback': goback})	

			c1 = 0
			c2 = 0
			c3 = 0
			c4 = 0

			for c in upass:
				if c >= "0" and c <= "9":
					c1 = 1
			for c in upass:
				if c >= "A" and c <= "Z":
					c2 = 1
			for c in upass:
				if c >= "a" and c <= "z":
					c3 = 1
			for c in upass:
				if c in '~!@#$%^&*()_+=-`':
					c4 = 1

			if c1 == 0 or c2 == 0 or c3 == 0 or c4 == 0:		

				txt = "The New Password should have at least 1 Capital Letter, 1 Small Letter, 1 Number and 1 Character!"
				goback = "/register"
				return render(request, 'front/msgbox.html', {'txt': txt, 'goback': goback})	

			if len(uuser) < 4:

				txt = "Your Username Must Be At Least 4 Characters!"
				goback = "/register"
				return render(request, 'front/msgbox.html', {'txt': txt, 'goback': goback})

			if len(upass) < 8:

				txt = "Your Password Must Be At Least 8 Characters!"
				goback = "/register"
				return render(request, 'front/msgbox.html', {'txt': txt, 'goback': goback})

			if len(User.objects.filter(username=uuser)) == 0 and len(User.objects.filter(email=uemail)) == 0:

				user = User.objects.create_user(username=uuser, email=uemail, password=upass)
				b = Manager(uuser=uuser, uemail=uemail)
				b.save()

	return render(request, 'front/register.html')

def answer_cm(request, pk):

	return render(request, 'back/answer_cm.html', {'pk': pk})