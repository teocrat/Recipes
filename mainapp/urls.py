from django.urls import path
from mainapp import views


urlpatterns = [
    path('', views.MainPageView.as_view())
]
