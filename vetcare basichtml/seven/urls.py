"""seven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from vet.views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", disp, name="disp"),
                  path("reg/?P<str:type>", start, name="adm"),
                  path("admr", db_Admin, name="admr"),
                  path("db_Doctor", db_Doctor, name="db_Doctor"),
                  path("db_Farmer", db_Farmer, name="db_Farmer"),
                  path("db_Animal", db_Animal, name="db_Animal"),
                  path("db_details", db_details, name="db_details"),
                  path("Ani_reg", Ani_reg, name="Ani_reg"),
                  path("Doct_r/?P<str:type>", Doct_r, name="Doct_r"),
                  path("d_l", d_l, name="d_l"),
                  path("pre_c", pre_c, name="pre_c"),
                  path("Farmer_Login/?P<str:type>", Farmer_Login, name="Farmer_Login"),
                  path("f_l", f_l, name="f_l"),
                  path("admin_details", admin_details, name="admin_details"),
                  path("req", req, name="req"),
                  path("Add_Animal", Add_Animal, name="Add_Animal"),
                  path("display", display, name="display"),
                  path("farmer_redirect/?P<str:k>", f_l1, name="farmer_redirect"),
                  path("doctor_redirect/?P<str:k>", doctor_redirect, name="doctor_redirect"),
                  path("displayf", displayf, name="displayf"),
                  path("displayd", displayd, name="displayd"),
                  path('doctorhome', doctorhome, name='doctorhome'),
                  #    path("'doctorhome'",'doctorhome',name="'doctorhome'"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
