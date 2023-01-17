from rest_framework import serializers

class MinionSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=100)

