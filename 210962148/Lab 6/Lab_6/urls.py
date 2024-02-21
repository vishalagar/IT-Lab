"""
Lab_6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path

<<<<<<< HEAD
from django.urls import include, path
import app.views

urlpatterns = [
    path('', app.views.calculator),
]
=======
urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
]
>>>>>>> 100c469513ab19e6a61241d50abef9d900f9d4ac
