from django.urls import path,include
from django.conf.urls.static import static
from .views import Registration, Request, AdminChart, DoctorReceive, pie, DoctorUpdate, DoctorHistory,\

    CustomerHistory, DoctorPie, DetailsPayment, PaySearch,Practice


from django.contrib import admin
urlpatterns = [
    path('registration/', Registration.as_view()),
    path('doctorreq/', Request.as_view()),
    path('doctorreceive/', DoctorReceive.as_view()),
    path('doctorupdate/', DoctorUpdate.as_view()),
    path('customerhistory/', CustomerHistory.as_view()),
    path('doctorhistory/', DoctorHistory.as_view()),
    path('detailspayment/', DetailsPayment.as_view()),
    path('paysearch/', PaySearch.as_view()),
    path('admin/', admin.site.urls),
    path('pie/', pie.as_view()),
    path('doctorpie/', DoctorPie.as_view()),

    path('adminchart/', AdminChart.as_view()),

    path('practice/', Practice.as_view()),


]