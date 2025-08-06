from django.urls import path
from . import views
from core import views
from .views import generate_order_summary
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.login_view, name='login'),  # Or any home route
    path('dashboard/', views.dashboard, name='dashboard'),  # ✅ ADD THIS
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.create_customer, name='create_customer'),
    path('customers/edit/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),

    # Order URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/edit/<int:order_id>/', views.edit_order, name='edit_order'),
    path('orders/edit/<int:order_id>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('api/generate-summary/', generate_order_summary, name='generate_summary'),
    
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('add/', views.add_product, name='add_product'),

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)