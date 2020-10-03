from django.urls import path
from . import views

urlpatterns = [
    # order(주문)
    path('order/',views.order,name='order'),
    path('order/orderlist/',views.order_list,name='order-list'),
    path('order/<int:id>/delete/', views.order_delete,name='order-delete'),
    path('order/update/',views.order_update,name='order-update'),

    path('add_item/<int:order_id>/<int:item_id>',views.add_item,name='add_item'),

    # delivery(배달)
    # path('delivery/',views.delivery,name='order'),
    # path('delivery/deliverylist/',views.delivery_list,name='delivery-list'),
    # path('delivery/<int:id>/delete/', views.delivery_delete,name='delivery-delete'),
    # path('delivery/update/',views.delivery_update,name='delivery-update'),

    path('item/',views.item_create,name='item'),
]