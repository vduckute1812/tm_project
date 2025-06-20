from typing import Dict

from rest_framework import serializers

from tm_utils.services.utils.function import save_data


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True

    def create(self, validated_data: Dict):
        return save_data(self._model, validated_data)

    def update(self, instance, validated_data: Dict):
        return save_data(self._model, validated_data, instance)

    @property
    def _model(self):
        model = getattr(self.Meta, "model", None)
        if not model:
            raise NotImplementedError("You must set 'model' in Meta class.")
        return model
