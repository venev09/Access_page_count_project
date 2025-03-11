from django.urls import path
from .views import count_view, reset_count_view, double_counter

urlpatterns = [
    path('counts/', count_view, name='count_view'),
    path('reset/', reset_count_view, name='reset_count_view'),
    path('double/', double_counter, name='double_count')
]