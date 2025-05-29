from typing import Dict

from rest_framework import serializers

from tm_club.models import TMDivision
from tm_club.services.division import DivisionService


class DivisionSerializer(serializers.Serializer):
    class Meta:
        model = TMDivision

    def create(self, validated_data: Dict):
        DivisionService.save(data=validated_data)

    def update(self, instance, validated_data: Dict):
        DivisionService.save(data=validated_data, instance=instance)
