from django.urls import path

from .views import (ProductViewCreate,ProductDetailUpdate,ProductDetailDelete,CategoryViewCreate,
                    CategoryDetailUpdate,CategoryDetailDelete,ReviewViewCreate,ReviewDetailUpdate,
                    ReviewDetailDelete)

urlpatterns = [
    path('api/v1/products/',ProductViewCreate.as_view()),
    path('api/v1/product/<int:pk>/',ProductDetailUpdate.as_view()),
    path('api/v1/product-delete/<int:pk>/',ProductDetailDelete.as_view()),
    path('api/v1/categories/',CategoryViewCreate.as_view()),
    path('api/v1/category/<int:pk>/',CategoryDetailUpdate.as_view()),
    path('api/v1/category-delete/<int:pk>/',CategoryDetailDelete.as_view()),
    path('api/v1/reviews/', ReviewViewCreate.as_view()),
    path('api/v1/review/<int:pk>/', ReviewDetailUpdate.as_view()),
    path('api/v1/review-delete/<int:pk>/', ReviewDetailDelete.as_view()),
]