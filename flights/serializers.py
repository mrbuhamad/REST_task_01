from rest_framework import serializers
from .models import Flight, Booking

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'destination', 'time', 'price',]



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'id',]

