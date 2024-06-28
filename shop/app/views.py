from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView

from .models import Category,Review,Product
from .serializers import CategorySerializer,ReviewSerializer,ProductSerializer


class ProductViewCreate(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailDelete(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailUpdate(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailDelete(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewCreate(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailUpdate(RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailDelete(RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
