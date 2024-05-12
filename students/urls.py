from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.filter_table, name="index"),
    
    path('add/', views.home, name="add"),

    path('update/', views.UpdateStudentForms, name="update"),

    path("delete/<int:id>/", views.delete, name="delete")
]
