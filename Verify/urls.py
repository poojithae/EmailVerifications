from django.urls import path  
from .views import *  
urlpatterns = [  
    #path('', home, name = 'home'),  
    #path('form/', index, name = 'index'), 
    path('signup/', signup, name='signup'), 
    path('activate/<uidb64>/<token>/', activate, name='activate'),    
]  