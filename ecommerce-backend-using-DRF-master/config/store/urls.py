from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    # user register and get token .. with that token user login and admin also getting token 

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'), 
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # # for viewing  all products... and everyone can view this products
     path('products/', ProductListView.as_view(), name='product-list'),

    # #for viewing the particuale product
     path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # # creating, updating and deletin the product .. only admin can do this 
     path('products/create/', ProductCreateView.as_view(), name='product-create'),
     path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
     path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # # for viewing the cart... means listing the cart
     path('cart/', CartListCreateView.as_view(), name='cart-list-create'),

    # #listin cart with id
     path('cart/<int:pk>/', CartItemUpdateDeleteView.as_view(), name='cart-item-detail'),

    #  # url for placing an order
     path('orders/place/', PlaceOrderView.as_view(), name='place-order'),

    #  # url for listing orders 
     path('orders/', UserOrderListView.as_view(), name='user-orders'),
   
]
