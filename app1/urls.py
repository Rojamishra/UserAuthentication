from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('',views.users,name='users'),
    path('signup',views.sign_up,name='signup'),
    path('login',views.log_in,name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.log_out,name='logout'),
    path('changepwd1',views.changepwd1,name='changepwd1'),
    path('changepwd2',views.changepwd2,name='changepwd2'),
    
]