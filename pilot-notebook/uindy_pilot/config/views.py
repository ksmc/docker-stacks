from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def goHome(request):
    context = {}
    return render(request, 'base/home.html', context)
