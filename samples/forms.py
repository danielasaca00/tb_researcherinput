from django import forms
from .models import Sample


class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = [
            'muestra_id',
            'fecha_muestreo',
            'lugar_muestreo',
            'tipo_muestra',
            'enfermedad_paciente',
            'secuenciacion',
            'fecha_secuenciacion',
            'plataforma',
            'longitud',
            'archivo',
            'notas',
        ]

        widgets = {
            'fecha_muestreo': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'fecha_secuenciacion': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'notas': forms.Textarea(
                attrs={'rows': 3, 'class': 'form-control'}
            ),
        }

    # OPCIONAL: aplica clase Bootstrap a todos los campos automáticamente
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if not isinstance(field.widget, forms.FileInput):
                field.widget.attrs.setdefault('class', 'form-control')

        # Campos booleanos → cambia a switch estilo Bootstrap
        self.fields['secuenciacion'].widget.attrs.update({
            'class': 'form-check-input'
        })
