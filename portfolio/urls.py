from django.urls import path

from .views import HomePageView, health_view

app_name = "portfolio"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("health/", health_view, name="health"),
]
