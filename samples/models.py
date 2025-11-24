from django.db import models
from django.contrib.auth.models import User


class Sample(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Usuario"
    )

    muestra_id = models.CharField("ID de Muestra", max_length=100)
    fecha_muestreo = models.DateField("Fecha de Muestreo")
    lugar_muestreo = models.CharField("Lugar de Muestreo (Ciudad, Estado)", max_length=200)
    tipo_muestra = models.CharField("Tipo de Muestra", max_length=100)
    enfermedad_paciente = models.CharField("Enfermedad del Paciente", max_length=200)

    secuenciacion = models.BooleanField("¿Secuenciación?", default=False)
    fecha_secuenciacion = models.DateField("Fecha de Secuenciación", null=True, blank=True)
    plataforma = models.CharField("Plataforma", max_length=100, null=True, blank=True)
    longitud = models.IntegerField("Longitud (bases)", null=True, blank=True)

    archivo = models.FileField(
        "Archivo de Secuenciación",
        upload_to="secuenciacion/",
        null=True,
        blank=True
    )

    notas = models.TextField("Notas", blank=True)

    class Meta:
        verbose_name = "Muestra"
        verbose_name_plural = "Muestras"

    def __str__(self):
        return f"{self.muestra_id}"


