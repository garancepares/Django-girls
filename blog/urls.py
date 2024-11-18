from django.urls import path
from . import views

urlpatterns = [
    path('', views.livre_list, name='livre_list'),
    path('livre/<str:id_livre>/', views.livre_detail, name='livre_detail'),
    path('livre/<str:id_livre>/?<str:message>', views.livre_detail, name='livre_detail_mes'),
]