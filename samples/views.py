from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
import csv

from .forms import SampleForm
from .models import Sample


# Añadir nueva muestra
@login_required
def add_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST, request.FILES)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.user = request.user
            sample.save()
            return redirect('my_samples')
    else:
        form = SampleForm()

    return render(request, 'samples/add_sample.html', {'form': form})


# Ver muestras del usuario
@login_required
def my_samples(request):
    samples = request.user.sample_set.all()
    return render(request, 'samples/my_samples.html', {'samples': samples})


# Editar muestra
@login_required
def edit_sample(request, pk):
    sample = get_object_or_404(Sample, pk=pk, user=request.user)

    if request.method == 'POST':
        form = SampleForm(request.POST, request.FILES, instance=sample)
        if form.is_valid():
            form.save()
            return redirect('my_samples')
    else:
        form = SampleForm(instance=sample)

    return render(request, 'samples/edit_sample.html', {'form': form})


# Eliminar muestra
@login_required
def delete_sample(request, pk):
    sample = get_object_or_404(Sample, pk=pk, user=request.user)

    if request.method == 'POST':
        sample.delete()
        return redirect('my_samples')

    return render(request, 'samples/delete_sample.html', {'sample': sample})


# Exportar CSV (solo administrador)
@staff_member_required
def export_samples_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="samples_export.csv"'

    writer = csv.writer(response)

    # Encabezados correctos
    writer.writerow([
        'ID',
        'Usuario',
        'Muestra ID',
        'Fecha de Muestreo',
        'Lugar',
        'Tipo de Muestra',
        'Enfermedad Paciente',
        'Secuenciación',
        'Fecha Secuenciación',
        'Plataforma',
        'Longitud',
        'Archivo',
        'Notas'
    ])

    # Filas de datos
    for sample in Sample.objects.all():
        writer.writerow([
            sample.id,
            sample.user.username,
            sample.muestra_id,
            sample.fecha_muestreo,
            sample.lugar_muestreo,
            sample.tipo_muestra,
            sample.enfermedad_paciente,
            sample.secuenciacion,
            sample.fecha_secuenciacion,
            sample.plataforma,
            sample.longitud,
            sample.archivo.url if sample.archivo else "",
            sample.notas,
        ])

    return response


# Dashboard
@login_required
def dashboard(request):
    sample_count = request.user.sample_set.count()

    return render(request, 'samples/dashboard.html', {
        'sample_count': sample_count
    })

def home(request):
    return render(request, 'home.html')  # o la plantilla que uses
