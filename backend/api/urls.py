from django.urls import path
from . import views

urlpatterns=[
    path('cms/',views.cmsView),
    path('cms/<int:pk>/',views.consultationDetailView),

    
    #administrator
    path('user/',views.UserView.as_view()),
    path('user/<int:pk>/',views.UserDetail.as_view())
]