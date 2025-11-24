from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from .models import Sample

class SampleAdmin(admin.ModelAdmin):
    list_display = (
        'muestra_id',
        'user',
        'fecha_muestreo',
        'tipo_muestra',
        'secuenciacion',
    )

    # Añadir URL personalizada para exportar CSV en admin
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'export-csv/',
                self.admin_site.admin_view(self.export_csv_view),
                name='samples_export_csv_admin'  # nombre interno
            )
        ]
        return custom_urls + urls

    def export_csv_view(self, request):
        # Redirige a la vista real export_samples_csv de la app
        return redirect('/export-csv/')  # ruta relativa de tu app

admin.site.register(Sample, SampleAdmin)




