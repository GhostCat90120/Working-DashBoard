from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpRequest
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required  #For function based view protection
from django.contrib.auth.mixins import LoginRequiredMixin  #For class based view protection
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import InsertDataForm
from .models import Inventory
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core import serializers

# Create your views here.
def home_view(request):
    return render(request, 'project_apps/home.html')

def features_view(request):
    return render(request, 'project_apps/features.html')

def about_view(request):
    return render(request, 'project_apps/about.html')

#REMOVE
def dashboard_view(request):
    month_param = request.GET.get('month', '2023-11')
    context = {}
    if month_param:
        month_inventory = Inventory.objects.filter(month=month_param).last()
        if month_inventory:
            context = {
                'month': month_inventory.month,
                'inventory_produce': month_inventory.inventory_produce,
                'cost_produce': month_inventory.cost_produce,
                'inventory_meat': month_inventory.inventory_meat,
                'cost_meat': month_inventory.cost_meat,
                'inventory_miscellaneous': month_inventory.inventory_miscellaneous,
                'cost_miscellaneous': month_inventory.cost_miscellaneous,
            }
    return render(request, 'project_apps/dashboard.html', context)

#REMOVE
def history_view(request):
    return render(request, 'project_apps/history.html')

#REMOVE
def create_view(request):
    return render(request, 'project_apps/create.html')


def save_to_dashboard(request):
    inventory = Inventory.objects.create(
        month=request.POST['month'],
        inventory_produce=request.POST['inventory_produce'],
        cost_produce=request.POST['cost_produce'],
        inventory_meat=request.POST['inventory_meat'],
        cost_meat=request.POST['cost_meat'],
        inventory_miscellaneous=request.POST['inventory_miscellaneous'],
        cost_miscellaneous=request.POST['cost_miscellaneous'],
    )
    inventory.save()
    return redirect('project_apps:dashboard')

#FIX
#Logged In views
#@login_required
#def dashboard_view(request):
   # return render(request, 'project_apps/dashboard.html')

#@login_required
#def create_view(request):
   # return render(request, 'project_apps/create.html')

#@login_required
#def history_view(request):
   # return render(request, 'project_apps/history.html')







def SignUp_View(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'project_apps/home.html')
    else:
        form = SignUpForm()
    return render(request, 'project_apps/signup.html', {'form': form})