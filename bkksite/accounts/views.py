from django.shortcuts import render
from django.core.urlresolvers import  reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DetailView,DeleteView
# from django.http import HttpResponse
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = 'accounts/signup.html'
