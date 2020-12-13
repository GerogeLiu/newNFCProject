from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import customerLoginForm, userLoginForm, userRegistraionForm

# Create your views here.
def index(request):
    return render(request, "account/index.html")


# Customer Login
def customerLogin(request):
    if request.method == "POST":
        login_form = customerLoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return redirect("/")
            else:
                return render(request, "account/customer_login.html", {"form": login_form, "error": "username or password is not correct"})
            
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = customerLoginForm()
        return render(request, "account/customer_login.html", {"form": login_form})

# End User Login
def userLogin(request):
    if request.method == "POST":
        login_form = userLoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return redirect("/")
            else:
                 return render(request, "account/customer_login.html", {"form": login_form, "error": "username or password is not correct"})
            
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = userLoginForm()
        return render(request, "account/user_login.html", {"form": login_form})


# End user sign up
def userRegister(request):
    if request.method == 'POST':
        user_form = userRegistraionForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect("account/userLogin")
        else:
            return render(request, "account/user_register.html", {"form": user_form})
    else:
        signup_form = userRegistraionForm()
        return render(request, "account/user_register.html", {"form": signup_form})
        

# log out
def userLogout(request):
    logout(request)
    return render(request, "account/logout.html")