from django_filters import rest_framework as filters
from .models import User


class UserFilter(filters.FilterSet):
    email_filter = filters.CharFilter(field_name="email", lookup_expr='contains')

    class Meta:
        model = User
        fields = ['username', 'email_filter', 'is_staff']