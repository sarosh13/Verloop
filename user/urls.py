from django.urls import path
from .views import ManagerListView,ManagerDetailView,StudentListView,StudentDetailView

urlpatterns = [
    path('api/manager/', ManagerListView.as_view()),
    path('api/manager/<int:pk>/', ManagerDetailView.as_view()),
    path('api/student/', StudentListView.as_view()),
    path('api/student/<int:pk>/', StudentDetailView.as_view()),
]