from tm_club.models import TMClub
from tm_utils.serializers.abstract import BaseSerializer
from rest_framework import serializers

class ClubSerializer(BaseSerializer):
    division_id = serializers.IntegerField(required=True)
    class Meta:
        model = TMClub
        fields = ["division_id", "name", "created_at", "updated_at"]
