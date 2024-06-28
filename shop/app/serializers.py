from rest_framework import serializers

from .models import Category,Product,Review


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        return instance



class ReviewSerializer(serializers.Serializer):
    comment = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment',instance.comment)
        return instance


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    image = serializers.ImageField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    created = serializers.DateField()
    term = serializers.DateField()
    category_id = serializers.IntegerField()
    comment_id = serializers.CharField(allow_null=True,allow_blank=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.image = validated_data.get('image',instance.image)
        instance.description = validated_data.get('description',instance.description)
        instance.price = validated_data.get('price',instance.description)
        instance.created = validated_data.get('created',instance.description)
        instance.term = validated_data.get('term',instance.description)
        instance.category_id = validated_data.get('category_id',instance.description)
        instance.comment_id = validated_data.get('comment_id',instance.description)
        return instance

