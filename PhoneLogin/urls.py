"""PhoneLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Account import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('login/',views.login_page,name = 'login'),
    path('login/',views.LoginApi.as_view(),name = 'login'),
    # path('register/',views.register,name='register'),
    # path('otp/<uid>/',views.otp),
    path('otp/<uid>/',views.OtpApi.as_view()),
    path('dashboard/',views.ProfileApi.as_view()),
    path('register/',views.RegistrationApi.as_view(),name = 'register'),
    path('event/',include(('Event.urls','event'),namespace='event')),
    # path('dashboard/',login_required(views.ProfileFill.as_view()),name = 'dashboard')
]
