from rest_framework import serializers
from .models import Track


class PointField(serializers.DictField):
    latitude = serializers.FloatField(min_value=-90, max_value=90)
    longitude = serializers.FloatField(min_value=-180, max_value=180)
    time = serializers.IntegerField()


class TrackSerializer(serializers.ModelSerializer):
    points = serializers.ListField(child=PointField(), allow_empty=False)

    class Meta:
        model = Track
        fields = ["id", "points", "created_at"]
        read_only_fields = ["id", "created_at"]
