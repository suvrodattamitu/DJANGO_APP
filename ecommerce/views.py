from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth import authenticate,login,logout,get_user_model

def home_page(request):
	context = {
		"title":"this is home.",
		"content":"where we are going to learn and know about home.",		
	}

	if request.user.is_authenticated:
		context["premium_content"] = "yeaaaaaa"
	return render(request,"home_page.html",context)

def about_page(request):
	context = {
		"title":"this is about page.",
		"content":"where we are going to learn and know about about page."
	}
	return render(request,"home_page.html",context)

def contact_page(request):
	contact_form = forms.ContactForm(request.POST or None)
	context = {
		"title":"this is contact.",
		"content":"where we are going to learn and know about contact.",
		"form":contact_form
	}

	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	if request.method == 'POST':
		print(request.POST.get('fullname'))
	return render(request,"contact/view.html",context)

def login_page(request):
	login_form = forms.LoginForm(request.POST or None)
	context = {
			"form":login_form
	}

	if login_form.is_valid():
		print(login_form.cleaned_data)

		username = login_form.cleaned_data.get("username")
		password = login_form.cleaned_data.get("password")
		user = authenticate(request,username=username,password=password)
		print(user)
		if user is not None:
			print(request.user.is_authenticated)
			login(request,user)
			return redirect("/")
		else:
			print("Error")

	return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
	register_form = forms.RegisterForm(request.POST or None)
	context = {
			"form":register_form
	}
	if register_form.is_valid():
		print(register_form.cleaned_data)
		username = register_form.cleaned_data.get("username")
		email = register_form.cleaned_data.get("email")
		password = register_form.cleaned_data.get("password")
		new_user = User.objects.create_user(username,email,password)
		print(new_user)
	return render(request,"auth/register.html",context)