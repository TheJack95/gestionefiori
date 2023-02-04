from .views import ItemsView
from django.urls import path

urlpatterns = [
    path('items/', ItemsView.as_view())
]
