from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['id', 'url', 'shortcode', 'created_at', 'updated_at', 'counter']
        read_only_fields = ['created_at', 'updated_at', 'counter']
    
    def validate_url(self, value):
        # Custom validation to check URL format
        if not (value.startswith('http://') or value.startswith('https://')):
            raise serializers.ValidationError("The format must start with http or https")
        return value

    def validate_shortcode(self, value):
        # Additional validation to ensure shortcode length
        if len(value) < 6:
            raise serializers.ValidationError("Shortcode must be at least 6 characters long")
        return value