# reservations/views.py
from django.shortcuts import render, redirect, render_to_response
from .models import Reservation
from .forms import ReservationForm

def home(request):
    return render(request, 'restaurant/index.html')
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_reservations')
    else:
        form = ReservationForm()
    return render(request, 'restaurant/create_reservation.html', {'form': form})

def list_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'restaurant/list_reservations.html', {'reservations': reservations})

# def custom_404(request, exception):
#     return render(request, '404/custom_404.html', status=404)

def handler404(request, *args, **argv):
    response = render_to_response('custom_404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response