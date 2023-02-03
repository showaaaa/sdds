from django.shortcuts import render
from .models import Ride
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

# rides = [
#     {
#         'destination': 'duke university',
#         'numberpassengers': '1',
#         'date': 'Jan 31, 2023',
#         'vehicletype': 'f1'
#     },
#     {
#         'destination': 'duke hospital',
#         'numberpassengers': '2',
#         'date': 'Jan 31, 2023'
#     }
# ]


def home(request):
    context = {
        'rides': Ride.objects.all()
    }
    return render(request, 'ride/home.html', context)

class RideOwnerListView(ListView):
    model = Ride
    template_name = 'ride/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rides'
    ordering = ['-date']
    def get_queryset(self):
        #return Ride.objects.filter(rideOwner=self.request.user or sharer.all().filter(username=self.request.user.username)).exclude(status=Ride.STATUS.completed)
        return Ride.objects.filter(rideOwner=self.request.user or sharer.all().filter(username=self.request.user.username).exists()).exclude(status=Ride.STATUS.completed)
    

class RideOwnerDetailView(DetailView):
    model = Ride


class RideOwnerCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    fields = ['destAddr', 'date', 'numPeople', 'vehicleType', 'shared', 'specRequest']
    # success_url = ''
    def form_valid(self, form):
        form.instance.rideOwner = self.request.user
        return super().form_valid(form)


class RideOwnerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ride
    fields = ['destAddr', 'date', 'numPeople', 'vehicleType', 'shared', 'specRequest']
    # success_url = ''
    def form_valid(self, form):
        form.instance.rideOwner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.rideOwner:
            return True
        return False


class RideOwnerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ride
    success_url = '/'
    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.rideOwner:
            return True
        return False
    

def about(request):
    return render(request, 'ride/about.html', {'title': 'About'})