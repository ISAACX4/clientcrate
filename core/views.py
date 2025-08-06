from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import openai
import json
from .models import Customer, Order, Product
from .forms import OrderForm, CustomerForm
from .forms import ProductForm

openai.api_key = settings.OPENAI_API_KEY


# ----------------------------------------
# HOME REDIRECT
# ----------------------------------------
def home(request):
    return redirect('login')


# ----------------------------------------
# USER REGISTRATION
# ----------------------------------------
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')

        return redirect('register')

    return render(request, 'core/register.html')


# ----------------------------------------
# USER LOGIN
# ----------------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'core/login.html')


# ----------------------------------------
# USER LOGOUT
# ----------------------------------------
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


# ----------------------------------------
# DASHBOARD VIEW
# ----------------------------------------
@login_required(login_url='login')
def dashboard(request):
    user = request.user
    customers_count = Customer.objects.filter(user=user).count()
    orders = Order.objects.filter(customer__user=user)
    orders_count = orders.count()
    pending_orders = orders.filter(status='pending').count()
    delivered_orders = orders.filter(status='delivered').count()
    recent_orders = orders.order_by('-created_at')[:5]

    return render(request, 'core/dashboard.html', {
        'user': user,
        'customers_count': customers_count,
        'orders_count': orders_count,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
        'recent_orders': recent_orders,
    })


# ----------------------------------------
# ORDER VIEWS
# ----------------------------------------
@login_required(login_url='login')
def create_order(request):
    form = OrderForm()
    form.fields['customer'].queryset = Customer.objects.filter(user=request.user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.fields['customer'].queryset = Customer.objects.filter(user=request.user)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            messages.success(request, 'Order created successfully.')
            return redirect('dashboard')

    return render(request, 'orders/create_order.html', {'form': form})


@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.filter(customer__user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required(login_url='login')

def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'orders/edit_order.html', {'form': form})
@login_required(login_url='login')
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer__user=request.user)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully.')
    return redirect('order_list')


# ----------------------------------------
# CUSTOMER VIEWS
# ----------------------------------------
@login_required(login_url='login')
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, 'Customer created successfully.')
            return redirect('customer_list')
    else:
        form = CustomerForm()

    return render(request, 'customers/create_customer.html', {'form': form})


@login_required(login_url='login')
def customer_list(request):
    customers = Customer.objects.filter(user=request.user).order_by('-id')
    return render(request, 'core/customer_list.html', {'customers': customers})


@login_required(login_url='login')
def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id, user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer updated successfully.')
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'core/edit_customer.html', {'form': form})


@login_required(login_url='login')
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id, user=request.user)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully.')
    return redirect('customer_list')


# ----------------------------------------
# AI-POWERED ORDER SUMMARY
# ----------------------------------------
@csrf_exempt
def generate_order_summary(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        products = data.get('products', '')
        quantity = data.get('quantity', '')
        customer = data.get('customer', '')

        prompt = f"Generate a brief order summary for a customer named {customer} who ordered {quantity} unit(s) of {products}."

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            summary = response['choices'][0]['message']['content']
            return JsonResponse({'summary': summary})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


# ----------------------------------------
# HELPER: GENERATE AI SUGGESTION FOR EDIT ORDER
# ----------------------------------------
def generate_ai_suggestion(order):
    prompt = f"""You're an assistant for a business dashboard. Based on this order, suggest what action should be taken.

Order Details:
- Customer: {order.customer.name}
- Status: {order.status}
- Description: {order.item_description}
- Created: {order.created_at}

Give a short suggestion (1–2 sentences).
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a helpful assistant for business managers."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Unable to generate suggestion at the moment."
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # <-- add request.FILES here
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # or wherever you want
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})     