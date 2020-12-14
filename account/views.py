from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import EndUserProfile, EndUserInfo
from .forms import customerLoginForm, userLoginForm, userRegistraionForm, \
    EndUserForm, EndUserInfoForm, EndUserProfileForm

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
                 return render(request, "account/user_login.html", {"form": login_form, "error": "username or password is not correct"})
            
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
            EndUserProfile.objects.create(user=new_user)
            EndUserInfo.objects.create(user=new_user)
            return redirect("/account/userLogin")
        else:
            return render(request, "account/user_register.html", {"form": user_form})
    else:
        signup_form = userRegistraionForm()
        return render(request, "account/user_register.html", {"form": signup_form})
        

# log out
def userLogout(request):
    logout(request)
    return render(request, "account/logout.html")


# show user information
@login_required(login_url='/account/userLogin/')
def endUser(request):
    user = User.objects.get(username=request.user.username)
    userProfile = EndUserProfile.objects.get(user=user)
    userInfo = EndUserInfo.objects.get(user=user)
    return render(request, "account/user_information.html", {"user": user, "userinfo": userInfo, "userprofile": userProfile})

# edit user information
@login_required
def endUserEdit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = EndUserProfile.objects.get(user=request.user)
    userinfo = EndUserInfo.objects.get(user=request.user)

    if request.method == "POST":
        user_form = EndUserForm(request.POST)
        userprofile_form = EndUserProfileForm(request.POST)
        userinfo_form = EndUserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd["email"])
            user.email = user_cd["email"]
            userprofile.birth = userprofile_cd["birth"]
            userprofile.phone = userprofile_cd["phone"]
            userprofile.address = userprofile_cd["address"]

            userinfo.school = userinfo_cd["school"]
            userinfo.company = userinfo_cd["company"]
            userinfo.profession = userinfo_cd["profession"]
            userinfo.aboutme = userinfo_cd["aboutme"]
            user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/user-information')

    else:
        user_form = EndUserForm(instance=request.user)
        userprofile_form = EndUserProfileForm(initial={"birth": userprofile.birth, \
            "phone": userprofile.phone, "address": userprofile.address})
        userinfo_form = EndUserInfoForm(initial={"school": userinfo.school, \
            "company": userinfo.company, "profession": userinfo.profession, \
            "aboutme": userinfo.aboutme})

        return render(request, "account/user_information_edit.html", {"user_form": user_form, \
            "userprofile_form": userprofile_form, "userinfo_form": userinfo_form})

# user image
@login_required(login_url='/account/userLogin/')
def userImage(request):
    if request.method == 'POST':
        img = request.POST['img']
        userinfo = EndUserInfo.objects.get(user=request.user)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request, 'account/imagecrop.html')