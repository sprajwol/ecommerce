from os import read
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from base.models import Product, Order, OrderItem, ShippingAddress


class UserSerialier(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerialier):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)

        return str(token.access_token)


class ProductSerialier(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShippingAddressSerialier(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerialier(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerialier(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shipingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerialier(items, many=True)

        return serializer.data

    def get_shipingAddress(self, obj):
        try:
            address = ShippingAddressSerialier(obj.shippingAddress, many=False)
        except:
            address = False

        return address

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerialier(user, many=False)

        return serializer.data
