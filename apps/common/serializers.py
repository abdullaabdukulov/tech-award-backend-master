from rest_framework import serializers


class RegionBaseSerializer(serializers.Serializer):
    guid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(read_only=True)


class RegionsSerializer(RegionBaseSerializer):
    pass


class DistrictsSerializer(RegionBaseSerializer):
    pass
