# define URL route for index() view
from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView, msg

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg, name='msg'),

]
