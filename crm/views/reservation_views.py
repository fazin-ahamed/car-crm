from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from crm.models import Reservation
from crm.forms import ReservationForm

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'crm/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'crm/reservation_detail.html', {'reservation': reservation})

def reservation_add(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            messages.success(request, 'Reservation added successfully.')
            return redirect(reverse('reservation_detail', args=[reservation.pk]))
    else:
        form = ReservationForm()
    return render(request, 'crm/reservation_form.html', {'form': form})

def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save()
            messages.success(request, 'Reservation updated successfully.')
            return redirect(reverse('reservation_detail', args=[reservation.pk]))
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'crm/reservation_form.html', {'form': form})
