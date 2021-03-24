from . import views
from django.urls import path

urlpatterns = [
    path('base',views.base,name="Base"),
    path('',views.index,name="index")
]