from django.conf.urls.static import static
from django.urls import path

from .views import Register, Login, DocInfo, AdminUserDetails, MyTokenObtainPairView, AdminUserSearch, AdminDoctorSearch

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('registration/', Register.as_view()),
    path('login/', Login.as_view()),
    path('doctordata/', DocInfo.as_view()),
    path('details/', DocInfo.as_view()),
    path('adminUserDetails/', AdminUserDetails.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('adminUserSearch/', AdminUserSearch.as_view()),
    path('adminDoctorSearch/', AdminDoctorSearch.as_view()),
    # path('adminUserDetails/', Docinfo.as_view()),
    # path('adminUserDetails/', Docinfo.as_view()),
    # path('adminUserDetails/', Docinfo.as_view()),

]
