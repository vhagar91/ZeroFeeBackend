from django_filters import rest_framework as filters
from .models import Listing


class ListingFilter(filters.FilterSet):
    nick = filters.CharFilter(field_name="nickname", lookup_expr='contains')

    class Meta:
        model = Listing
        fields = ['nick']