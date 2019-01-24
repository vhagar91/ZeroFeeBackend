from rest_framework import permissions
from rest_framework_api_key.models import APIKey


class OnlyAPIPermission(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        try:
            api_key = request.query_params.get('apikey', False)
            return APIKey.objects.filter(id=api_key).exists()
        except:
            return False