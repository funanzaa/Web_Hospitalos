from django.shortcuts import render
from django.core.urlresolvers import  reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DetailView,DeleteView

from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'index.html'
