from tm_club.models import TMClub
from tm_utils.serializers.abstract import BaseSerializer


class ClubSerializer(BaseSerializer):
    class Meta:
        model = TMClub
