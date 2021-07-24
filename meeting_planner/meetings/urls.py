from django.urls import path

from . import views

# url mappings for all views in the meetings app

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.room_list, name="rooms"),
    path('new', views.new, name='new')
]