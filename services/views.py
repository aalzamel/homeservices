from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Product
from address.models import Area, Address
from .forms import UserSignUp, UserLogin
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def home_view(request):
	category = Category.objects.all()
	area = Area.objects.all()

	context = {
		'category': category,
		'area': area,
	}


	return render(request, "home.html", context)



def category_view(request):
	category = Category.objects.all()

	context = {
		'category': category,
	}


	return render(request, "category_view.html", context)


def products(request):
	category = request.GET.get('category', None)
	area = request.GET.get('area', None)


	products_list = Product.objects.filter(category__name=category, area__name=area)
	if len(products_list) < 1:
		products_list = Product.objects.filter(category__name=category)
		if len(products_list) < 1:
			products_list = Product.objects.filter(area__name=area)
			if len(products_list) < 1:
				products_list = Product.objects.all()


	# if category is not None:
	# 	if area is not None:
	# 		products_list = Product.objects.filter(category__name=category, area__name=area)

	# 	if area is None:
	# 		products_list = Product.objects.filter(category__name=category)

	# if category is None:
	# 	if area is None:
	# 		products_list = Product.objects.all()
	# 	if area is not None:
	# 		products_list = Product.objects.filter(area__name=area)

	context = {
		'products_list': products_list,
	}


	return render(request, "products_list.html", context)



def product_detail(request, product_name):
	item = get_object_or_404(Product, name=product_name)

	context = {
		"items": item,

	}

	return render(request, "detail.html", context)




def usersignup(request):
	context = {}
	form = UserSignUp()
	context['form'] = form

	if request.method == "POST":
		form = UserSignUp(request.POST)

		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password

			user.set_password(password)
			user.save()
			auth = authenticate(username=username, password=password)
			login(request, auth)
			return redirect("homeservices:home_view")
		messages.warning(request, form.errors)
		return redirect("homeservices:usersignup")
	return render(request, "signup.html", context)



#login form

def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form

	if request.method == "POST":
		form = UserLogin(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			auth = authenticate(username=username, password=password)
			if auth is not None:
				login(request, auth)
				return redirect("homeservices:home_view")
			messages.warning (request, 'Incorrect username/password combination')
			return redirect("homeservices:userlogin")
		messages.warning(request, form.errors)
		return redirect("homeservices:userlogin")
	return render(request, "login.html", context)



def userlogout(request):
	logout(request)
	return redirect("homeservices:home_view")



