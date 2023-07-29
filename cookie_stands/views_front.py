from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand

class CookieStandListView(LoginRequiredMixin, ListView):
  template_name = 'cookie_stands/cookie_stands_list.html'
  model = CookieStand
  context_object_name = 'cookie_stands'
  
class CookieStandDetailView(LoginRequiredMixin, DetailView):
  template_name = 'cookie_stands/cookie_stands_detail.html'
  model = CookieStand
  
class CookieStandCreateView(LoginRequiredMixin, CreateView):
  template_name = 'cookie_stands/cookie_stands_create.html'
  model = CookieStand
  fields = ['location', 'owner', 'description', 'hourly_sales', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale'] # "__all__" for all of them
  
class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
  template_name = 'cookie_stands/cookie_stands_update.html'
  model = CookieStand
  fields = '__all__'
  
class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
  template_name = 'cookie_stands/cookie_stands_delete.html'
  model = CookieStand
  success_url = reverse_lazy('cookie_stands_list')
