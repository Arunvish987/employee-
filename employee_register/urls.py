from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'),
    path('update/<int:pk>/', views.employee_update, name='employee_update'),
    path('list/', views.employee_list, name='employee_list'),

]