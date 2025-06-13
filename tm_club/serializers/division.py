from tm_club.models import TMDivision
from tm_utils.serializers.abstract import BaseSerializer


class DivisionSerializer(BaseSerializer):
    class Meta:
        model = TMDivision
