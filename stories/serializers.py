from rest_framework import serializers

from stories.models import Media, Story


class StorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    media = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Story
        fields = (
            'id', 'created', 'title', 'why', 'when', 'where', 'who', 'author',
            'fb_id', 'media')
        read_only_fields = ('created', 'id', 'media')


class UserStoriesSerializer(serializers.ModelSerializer):
    media = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Story
        fields = (
            'id', 'created', 'title', 'why', 'when', 'where', 'who', 'author',
            'fb_id', 'media')
        read_only_fields = ('created', 'id', 'media')
        lookup_field = 'fb_id'



class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('story', 'file')

    def create(self, validated_data):
        story_id = validated_data.pop('story')
        return Media.objects.create(story=story_id, **validated_data)
