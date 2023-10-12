from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [ 
            # path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login_view'),
            path('',views.login_view,name='login_view'),
            path('login_view',views.login_view,name='login_view'),
            path('sign_up',views.sign_up,name='sign_up'),
            path('home',views.home,name='home'),       
            path('chat_view/', views.chat_view, name='chat_view'),
            path('timer', views.timer, name='timer'),     
            path('cripto', views.cripto, name='cripto'),     
            path('profile', views.profile, name='profile'),     
            path('message/<int:id>/',views.message,name='message'),
            # path('dash',views.dash,name='dash'),
            # path('add_candidate',views.add_candidate,name='add_candidate'),
            # path('candidates_details',views.candidates_details,name='candidates_details'),
            # path('delete_candidate/<int:id>/', views.delete_candidate, name='delete_candidate'),
            # path('member_dash/<int:id>/',views.member_dash,name='member_dash'),
            ]