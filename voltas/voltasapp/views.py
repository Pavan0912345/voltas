from django.shortcuts import redirect, render
from .models import Voltas_product_details
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MyModelForm

def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = MyModelForm()
    return render(request, 'template.html', {'form': form})

def coming_soon(request):
    # all_data = Voltas_product_details.objects.all()  # Fetch all your data
    data = Voltas_product_details.objects.all().values(
        'source_name', 'source_id', 'category', 'product_name', 'product_url',
        'mrp', 'deal_price', 'discount_percentage', 'seller_name', 'seller_name_and_id',
        'seller_address', 'bank_offers', 'offers', 'brand', 'model_name', 'capacity',
        'colour', 'technical_details', 'seller_details', 'seller_actual_name', 'seller_id',
        'channel_sku', 'channel', 'model_number', 'location', 'zipcode', 'mop_modified',
        'created_at', 'modified_at'
    )
    paginator = Paginator(data, 20)  # Show 10 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    return render(request, 'coming_soon.html',  {'page_obj': page_obj})
# def container(request):
#     return coming_soon(request)



def container(request):
    data = Voltas_product_details.objects.all().values(
        'source_name', 'source_id', 'category', 'product_name', 'product_url',
        'mrp', 'deal_price', 'discount_percentage', 'seller_name', 'seller_name_and_id',
        'seller_address', 'bank_offers', 'offers', 'brand', 'model_name', 'capacity',
        'colour', 'technical_details', 'seller_details', 'seller_actual_name', 'seller_id',
        'channel_sku', 'channel', 'model_number', 'location', 'zipcode', 'mop_modified',
        'created_at', 'modified_at'
    )
    paginator = Paginator(data, 20)  # Show 10 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'coming_soon.html', {'page_obj': page_obj})
# def container(request):
#     page_obj = coming_soon(request)  # Fetch mopv_summary data
#     return render(request, 'container.html', {'page_obj': page_obj})


def soon(request):
    return render(request,'soon.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('container')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page after logout
def logout_view(request):
    # Your logout logic here
    # For example, you can clear the session
    request.session.flush()
    # Redirect to login page or display a logout confirmation message
    return HttpResponse("Logged out successfully")