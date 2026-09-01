from django.urls import path
from . import views

urlpatterns=[
    #doctor
    path('cms/',views.cmsView),
    path('cms/<int:pk>/',views.consultationDetailView),
    path('PrescribedLab/',views.PrescribedLabView.as_view()),
    path('PrescribedLabDetailView/<int:pk>/',views.PrescribedLabDetailView.as_view()),
      
    
    #administrator
    path('user/',views.UserView.as_view()),
    path('user/<int:pk>/',views.UserDetail.as_view()),
    path("staff/",views.StaffListCreateView.as_view()),
    path("staff/<int:pk>/",views.StaffDetailView.as_view()),
    path("doctors/",views.DoctorListCreateView.as_view()),
    path("doctors/<int:pk>/",views.DoctorDetailView.as_view()),

    #receptionist
    path("patients/",views.PatientListCreateView.as_view()),
    path("patients/<int:pk>/",views.PatientDetailView.as_view()),

    
]