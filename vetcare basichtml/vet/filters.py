import django_filters
from .models import *

class DetailsFilter(django_filters.FilterSet):
    class Meta:
        model = Details1
        fields = '__all__'