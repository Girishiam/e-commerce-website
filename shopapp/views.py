from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from shopapp.models import Product
# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'shopapp/home.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shopapp/productdetail.html'
