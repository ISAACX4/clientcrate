from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Order, Customer, Product
from django import forms
from .models import Order


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'customer',
            'product',
            'status',
            'delivery_date',
            'item_description',
            'is_paid',
        ]
        widgets = {
            'product': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'delivery_date': forms.DateInput(attrs={'type': 'date', 'class': 'input input-bordered w-full'}),
            'item_description': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full'}),
            'status': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'customer': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input w-full rounded-xl border border-[#d4dbe2] bg-gray-50 h-14 p-[15px] placeholder-[#5c728a]',
                'placeholder': 'Enter customer name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input w-full rounded-xl border border-[#d4dbe2] bg-gray-50 h-14 p-[15px] placeholder-[#5c728a]',
                'placeholder': 'Enter phone number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input w-full rounded-xl border border-[#d4dbe2] bg-gray-50 h-14 p-[15px] placeholder-[#5c728a]',
                'placeholder': 'Enter email address'
            }),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-14 p-4',
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-32 p-4',
                'placeholder': 'Enter product description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-14 p-4',
                'placeholder': 'Enter price'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-input w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-14 p-4',
                'placeholder': 'Enter available stock'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-input w-full rounded-xl border border-[#cedbe8] bg-slate-50 p-4'
            }),
        }
        
    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input w-full rounded-xl border border-[#d0dbe7] bg-slate-50 h-14 p-[15px]'}),
            'description': forms.Textarea(attrs={'class': 'form-input w-full rounded-xl border border-[#d0dbe7] bg-slate-50 min-h-36 p-[15px]'}),
            'price': forms.NumberInput(attrs={'class': 'form-input w-full rounded-xl border border-[#d0dbe7] bg-slate-50 h-14 p-[15px]'}),
            'stock': forms.NumberInput(attrs={'class': 'form-input w-full rounded-xl border border-[#d0dbe7] bg-slate-50 h-14 p-[15px]'}),
            'category': forms.Select(attrs={'class': 'form-input w-full rounded-xl border border-[#d0dbe7] bg-slate-50 h-14 p-[15px]'}),
        }