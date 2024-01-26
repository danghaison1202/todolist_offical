from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete,name='delete'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name="register"),
    # path('', views.unauth_home, name="home"),
    path('profile/<username>', views.profile, name='profile'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),

]
