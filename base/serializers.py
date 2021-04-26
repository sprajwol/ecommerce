from rest_framework import serializers
from django.contrib.auth.models import User

from base.models import Product

class ProductSerialier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'