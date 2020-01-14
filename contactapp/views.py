from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from .forms import *
from django.http import *


# Create your views here.

def Home(request):
    count = contact_list.objects.all().count()
    return render(request,'contactapp/Home.html',{'count':count})

def Register(request):
    if request.method == 'POST' :
        uname = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        u = User.objects.create_user(username=uname , first_name=fname , last_name=lname , email=email , password=password)
        messages.success(request,f'Account Created For {uname}!')
        if uname == uname:
        	return redirect('Register')
    return render(request,'contactapp/Register.html')

def Login(request):
    if request.method == 'POST' :
        uname = request.POST['uname']
        password = request.POST['pass']
        u = authenticate(request , username=uname , password=password)
        if u is not None :
            msg = 'valid user'
            login(request , u)
            return redirect('Home')
        else:
            msg = "invalid user or password"
        context = {
        		"msg" : msg
        	}
    return render(request,'contactapp/Login.html')

@login_required
def Logout(request):
    logout(request)
    return render(request,'contactapp/Logout.html')

@login_required
def Contact(request):
    contact = contact_list.objects.all()

    return render(request,'contactapp/Contact.html',{'contact':contact})

@login_required
def Contact_Insert(request):
    print("Contact Is Saved")
    country = Country.objects.all()
    state = State.objects.all()
    city = City.objects.all()
    if request.method == 'POST':
        form = contact_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/Contact")
    else:
        form = contact_form()
    return render(request,'contactapp/Insert.html',{'form':form,'Country':country,'State':state,'City':city})

@login_required
def Edit(request,c_id):
    contact = contact_list.objects.get(c_id=c_id)
    return render(request,'contactapp/Edit.html',{'contact':contact})
@login_required
def Update(request,c_id):
    contact = contact_lists.objects.get(c_id=c_id)
    form = contact_form(request.POST,instance=contact)
    if form.is_valid():
        form.save()
        return HttpResponseredirect("/Contact")
    return render(request,'contactapp/Edit.html',{'contact':contact})

def Delete(request,c_id):
    contact = contact_list.objects.get(c_id=c_id)
    contact.delete()
    return redirect('Contact')