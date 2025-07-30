from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Order, Customer

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'item_description', 'status', 'delivery_date', 'is_paid']
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-select w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-14 p-4'
            }),
            'item_description': forms.Textarea(attrs={
                'class': 'form-textarea w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-36 p-4',
                'placeholder': 'Enter item description'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-14 p-4'
            }),
            'delivery_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input w-full rounded-xl border border-[#cedbe8] bg-slate-50 h-14 p-4'
            }),
            'is_paid': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-blue-600 border-gray-300 rounded focus:ring-0'
            }),
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
