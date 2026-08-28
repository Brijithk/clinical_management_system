from django.urls import path
from . import views

urlpatterns=[
    path('cms/',views.cmsView),
    path('cms/<int:pk>/',views.consultationDetailView),
]