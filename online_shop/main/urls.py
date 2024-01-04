from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('config/', views.stripe_config, name='stripe-config'),
    path('buy/<int:pk>/', views.create_item_checkout_session,
         name='buy'),
    path('orders/buy/<int:pk>/', views.create_order_checkout_session,
         name='order_buy'),
    path('success/', views.SuccessView.as_view(), name='success-view'),
    path('cancelled/', views.CancelledView.as_view(), name='cancelled-view'),
    path('item/', views.ItemListView.as_view(), name='items_list'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('orders/', views.OrderListView.as_view(), name='orders_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
]
