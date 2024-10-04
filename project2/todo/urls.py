from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('list',views.list),
    path('detail',views.detail)
]