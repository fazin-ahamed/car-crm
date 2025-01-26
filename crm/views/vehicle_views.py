from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from crm.models.vehicle import Vehicle
from crm.forms.vehicle_form import VehicleForm

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})

def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('vehicle_list'))
    else:
        form = VehicleForm()
    return render(request, 'vehicle_form.html', {'form': form})

def vehicle_edit(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect(reverse('vehicle_detail', args=[pk]))
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicle_form.html', {'form': form})
