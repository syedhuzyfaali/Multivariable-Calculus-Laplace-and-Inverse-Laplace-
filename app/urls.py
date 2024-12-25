from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('demo/', demo, name='demo'),
    path('solve-laplace/', solve_laplace, name='solve_laplace'),
    path('original-function/', original_function, name='original_function'),
    path('first-order-derivative/', first_order, name='first_order'),
    path('second-order-derivative/', second_order, name='second_order'),
    path('integration-property/', integration_property, name='integration_property'),
]