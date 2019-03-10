from django.urls import path, include
from testurl import views

urlpatterns = [
 #   path('', views.home, name='home'),
    # site.com/user/12
    path('user/<int:num>', views.home,name='home')
]
