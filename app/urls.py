
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('success/', views.success, name='success'),
    path('dashboard/', views.dashboard, name='dashboard'),
]