from django.urls import path
from . import views

urlpatterns = [
    path('tour/', views.TourListAPIView.as_view()),
    path('tour/<int:pk>/', views.TourRetrieveAPIView.as_view())
]
