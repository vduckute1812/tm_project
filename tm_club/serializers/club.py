from typing import Dict

from rest_framework import serializers

from tm_club.models import TMClub
from tm_club.services.club import ClubService


class ClubSerializer(serializers.Serializer):
    class Meta:
        model = TMClub

    def create(self, validated_data: Dict):
        ClubService.save(data=validated_data)

    def update(self, instance, validated_data: Dict):
        ClubService.save(data=validated_data, instance=instance)
