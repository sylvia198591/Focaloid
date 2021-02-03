"""BMS URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.shortcuts import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Userdetail import views
from Userdetail.views import *
urlpatterns = [
    path('Registration',views.createUser.as_view(),name="User_create"),
    # path('Registration', lambda request:(views.createUser.as_view())\
    #         if ('Username' not in request.session) else \
    #             redirect('User_home'),name="User_create"),
    path('Login', views.loginUser.as_view(), name="User_login"),
    path('Logout', lambda request:redirect('User_home') \
        if ('Username' not in request.session) else \
            (logoutUser(request)), name="User_logout"),
    # path('Home', index.html, name="Home"),
    path("Loggedin",lambda request:render(request,"index.html"),name="User_home_loggedin"),
    path("", lambda request: redirect('User_login') \
        if ('Username' not in request.session) else \
        redirect('User_home_loggedin')
         , name="User_home"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)