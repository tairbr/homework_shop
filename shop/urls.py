
from django.urls import path

from .views import *

app_name = 'shop'

urlpatterns = [
    path('product/create', ProductCreateView.as_view()),
    path('all/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductRetrieveView.as_view()),
    path('product/delete/<int:pk>/', ProductDestroyView.as_view()),
]

