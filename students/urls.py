from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.filter_table, name="index"),
    
    path('add/', views.home, name="add"),

    path('add/<int:id>/', views.update, name="update"),

    path("delete/<int:id>/", views.delete, name="delete"),

    path('filter/', views.filter_table, name="filter")
]
