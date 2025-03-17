from rest_framework import serializers
from api.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'stock'
        )

    def validate_price(self, value):
        '''
        @description: this field level validation is used for the price field \
                      to ensure the price is above 0.0
        '''

        if value <= 0:
            raise serializers.ValidationError(
                "price must be greater than 0.0"
            )
        return value