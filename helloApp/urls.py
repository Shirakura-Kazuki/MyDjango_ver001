from django.urls import path
from . import views

urlpatterns = [
    path('',views.item_list , name='item_list'),    # home.html
    path('add/', views.add_item, name='add_item'),  # add_item.html
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'), # edit_item.html
]