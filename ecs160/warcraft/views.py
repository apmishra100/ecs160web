from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Context
from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm

import re

# Create your views here.

def index(request):
    template = loader.get_template('warcraft/index.html')
    return HttpResponse(template.render())
    

def prototype_form(request):
    template = loader.get_template('warcraft/prototype_form.html')
    return HttpResponse(template.render())

def prototype(request):
    error = False
    message=""
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
            message = "BAD INPUT"
            return render(request, 'warcraft/prototype_form.html', {'error':error, 'message':message})
        else:
            message = '%s' %request.GET['q']
            if message == "":
                message = "BAD INPUT"
                return render(request, 'warcraft/prototype_form.html', {'error':True, 'message':message})
            else:
                return render(request, 'warcraft/prototype_form.html', {'error':error, 'message':message})
    else:
        return render(request, 'warcraft/prototype_form.html', {'error':error, 'message':message})


def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('warcraft/login.html', c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
        
def logout(request):
    auth.logout(request)
    return render_to_response('warcraft/logout.html')

def loggedin(request):
    return render_to_response('warcraft/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('warcraft/invalid_login.html')
    
    
def register_user(request):
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            avatar = request.FILES['avatar']
            avatar.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            args['form'] = form
    return render_to_response('warcraft/register.html', args)

def register_success (reqest):
    return render_to_response('warcraft/register_success.html')

def internalLogin (request):
    if request.method == 'GET':
        username = request.META['HTTP_USERNAME']
        password = request.META['HTTP_PASSWORD']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/loggedin')
        else:
            return HttpResponseRedirect('/accounts/invalid')
        return render(request, 'warcraft/internalLogin.html', {'username': dummy, 'password': passdummy})
