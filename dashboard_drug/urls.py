# 23.04.17 추가
from django.urls import path
from dashboard_drug import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name="dashboard"),
]
