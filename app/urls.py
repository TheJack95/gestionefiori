from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('add/<int:id>', views.update_item, name='updateitem'),
    path('add/', views.add, name='add'),
]
