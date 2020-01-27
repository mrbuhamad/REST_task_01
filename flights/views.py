from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from datetime import date

class FlightsView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsSerializer


class BookingsView(ListAPIView):

    queryset = Booking.objects.filter(date__gte=date.today())
    serializer_class = BookingSerializer



