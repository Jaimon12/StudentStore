from django.urls import path,include
from store import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('courses/', views.course, name='courses'),
     path('logout/', views.logout, name='logout'),
    path('form/', views.information_form, name='form'),
    path('success/<str:purpose>/', views.success_page, name='success_page'),
]