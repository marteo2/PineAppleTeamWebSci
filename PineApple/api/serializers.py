from rest_framework import serializers
from btcdata.models import PriceData


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PriceData
        fields = {"id", "time", "price"}
