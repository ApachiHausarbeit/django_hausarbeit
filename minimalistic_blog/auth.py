# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

def logout_view(request):
    logout(request)
    return render(request, 'index.html')

""" Reference:
    http://www.djangobook.com/en/2.0/chapter14.html """
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/blog/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })
