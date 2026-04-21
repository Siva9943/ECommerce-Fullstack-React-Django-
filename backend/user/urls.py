from django.urls import path
from .views import *
urlpatterns=[
    path('register/', SignupUser.as_view(), name='signup_data'),
    path('login/', LoginUser.as_view(), name='login_data'),

]