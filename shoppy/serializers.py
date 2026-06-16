from rest_framework import serializers
from .models import Product, Category, Owner, Cart, Element


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    owner = OwnerSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(
        queryset=Owner.objects.all(), source='owner', write_only=True
    )

    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    product_title = serializers.CharField(source='product.title', read_only=True)

    class Meta:
        model = Element
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    elements = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
