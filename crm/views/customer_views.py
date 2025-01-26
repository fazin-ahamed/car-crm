from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from crm.models.customer import Customer
from crm.forms.customer_form import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect(reverse('customer_detail', args=[customer.pk]))
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            return redirect(reverse('customer_detail', args=[customer.pk]))
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})
