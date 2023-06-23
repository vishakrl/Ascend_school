"""
URL configuration for Ascend_school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('log/',views.login,name="loginpage"),
    path('reg/',views.register,name='registerpage'),
    path('logout/',views.logout),
    path('about/',views.about),
    path('admit/',views.admission,name='admissionpage'),
    path('table/',views.table),
    path('table/table_s/',views.testsub_s),
    path('table/table_c/',views.testsub_c),
    path('table/table_h/',views.testsub_h),
    

]
