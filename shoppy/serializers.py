from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Product, Category, Owner, Cart, Element, Profile

User = get_user_model()


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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'full_name', 'phone', 'address',
                  'favorite_category', 'hiking_experience']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile', 'is_staff']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        profile = instance.profile
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()

        return instance


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
        )
        return user
