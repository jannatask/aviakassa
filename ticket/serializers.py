from rest_framework import serializers

from .models import Category, Ticket

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'