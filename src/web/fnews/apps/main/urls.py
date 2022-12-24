from django.urls import path
from apps.main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('prediction/', views.prediction, name="prediction")
]