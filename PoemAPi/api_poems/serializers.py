from rest_framework import serializers
from .models import Poem


# using serializers
# class PoemSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     poem = serializers.CharField(max_length=1000)
#     poet = serializers.CharField(max_length=100)
#     likes = serializers.IntegerField()
#     date = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Poem.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.poem = validated_data.get("poem", instance.poem)
#         instance.poet = validated_data.get("poet", instance.poet)
#         instance.date = validated_data.get("date", instance.date)
#         instance.save()
#         return instance


# using modelSerializer

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ['id', 'title', 'poem', 'poet', 'likes']

