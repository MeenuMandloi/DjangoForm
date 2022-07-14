from django.shortcuts import render, redirect
from app1.models import Usertable
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.urls import reverse


def index(request):
    return render(request, "index.html")


def admin_index(request):
    return render(request, "admin.html")


def Register(request):
    if request.method == "POST":

        email = request.POST.get('email')
        print("Email", request.user.email)
        if Usertable.objects.filter(email=email).exists():
            return HttpResponse("User Already Registered")
        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            gender_selection = request.POST.get('gender_selection')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            email = request.POST.get('email')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            user = Usertable.objects.create(firstname=firstname, lastname=lastname, gender=gender_selection,
                                            phone=phone, address=address, email=email, password=password)
            if user:
                if password != repassword:
                    return HttpResponse("Password does not match")
                else:
                    return render(request, "login.html")  # context
    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        super_user = User.objects.filter(email=email)
        user = authenticate(request, email=email, password=password)
        # login(request, user)
        print("pwd", password)
        check_user = Usertable.objects.filter(email=email)
        if check_user:
            for data in check_user:
                if data.email == email:
                    if data.password == password:
                        request.session['email'] = email
                        user = Usertable.objects.get(email=email)
                        print("Email", email)
                        context = {'user': user}
                        return render(request, "myprofile.html", context)
                    else:
                        return HttpResponse('Please enter valid Password.')
                else:
                    return HttpResponse('Please enter valid email.')
        else:
            for data in super_user:
                if data.email == email:
                    if check_password(password, data.password):
                        request.session['email'] = email
                        # user = Usertable.objects.all()
                        # context = {'user': user}
                        return render(request, "admin.html")
                    else:
                        return HttpResponse('Please enter valid Password.')
                else:
                    return HttpResponse('Please enter valid email.')

    return render(request, 'login.html')


def userdetail(request):
    user = Usertable.objects.all()
    context = {'user': user}
    return render(request, "userdetail.html", context)


def admindetail(request):
    return render(request, "admindetail.html")


def delete(request, id):
    user = Usertable.objects.get(id=id)
    user.delete()
    return redirect('userdetail')


def update(request,id):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender_selection = request.POST.get('gender_selection')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Usertable.objects.get(id=id)
        user.firstname = firstname
        user.lastname = lastname
        user.gender = gender_selection
        user.phone = phone
        user.address = address
        user.email = email
        user.password = password
        user.save()
        return redirect('userdetail')
    user = Usertable.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, "update.html", context)


"""
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        super_user = User.objects.filter(email=email)
        user = authenticate(request, email=email, password=password)
        # login(request, user)
        print("pwd", password)
        check_user = Usertable.objects.filter(email=email)
        if check_user:
            for data in check_user:
                if data.email == email:
                    if data.password == password:
                        request.session['email'] = email
                        user = Usertable.objects.get(email=email)
                        print("Email", email)
                        context = {'user': user}
                        return render(request, "myprofile.html", context)
                    else:
                        return HttpResponse('Please enter valid Password.')
                else:
                    return HttpResponse('Please enter valid email.')
        else:
            for data in super_user:
                if data.email == email:
                    if check_password(password, data.password):
                        request.session['email'] = email
                        user = Usertable.objects.all()
                        context = {'user': user}
                        return render(request, "admin.html", context)
                    else:
                        return HttpResponse('Please enter valid Password.')
                else:
                    return HttpResponse('Please enter valid email.')

    return render(request, 'login.html')
"""
