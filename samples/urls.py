from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_sample, name='add_sample'),
    path('my-samples/', views.my_samples, name='my_samples'),
    path('edit/<int:pk>/', views.edit_sample, name='edit_sample'),
    path('delete/<int:pk>/', views.delete_sample, name='delete_sample'),

    # Exportar CSV (solo admin)
    path('export-csv/', views.export_samples_csv, name='export_samples_csv'),
]
