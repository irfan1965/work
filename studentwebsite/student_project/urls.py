"""student_project URL Configuration

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
from Student.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("h/",disp),
    path("search_id",search_roll,name="find"),
    path("branch",search_branch,name="branch"),
    path("marks",marks,name="thes"),
    path("",first),
    path("cse",cse,name="cse"),
    path("info",info,name="info"),
    path("eee",eee,name="eee"),
    path("Pharmacy",Pharmacy,name="Pharmacy"),
    path("mechanical",mechanical,name="mechanical"),
    path("brn",branch,name="brn"),
    path("marks/",details,name="sucess"),
    path("Student/views/",intra,name="roll"),
    path("s_f",s_f,name="s_f"),
    path("rgt/",rgt,name="the"),
    path("reg/",fun,name="xyz"),
    path("qw/",bar,name="br"),
    path("djufd/",disp1),
    path("sad",bar, name="qwerty"),
    path("sid",sid,name="sid"),
    path("home",home,name="home"),
    path("branch1",branch1,name="branch1")
    # path("ewdf",)
    #   url(r'^media/(?P<path>.*)$', serve, {
    #         'document_root': settings.MEDIA_ROOT
    #     })



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
