from rest_framework import serializers

from shortener.models import ShortURL
from shortener.services import get_short_url


class ShortURLSerializer(serializers.ModelSerializer):
    short_url = serializers.URLField(
        read_only=True,
        label='Короткая ссылка',
    )

    class Meta:
        model = ShortURL
        fields = '__all__'

    def create(self, validated_data):
        """Создаем короткую ссылку при создании модели."""
        short_url = get_short_url(validated_data['url'])
        return ShortURL.objects.create(short_url=short_url, **validated_data)

    def update(self, instance, validated_data):
        """Создаем короткую ссылку при обновлении модели."""
        instance.url = validated_data['url']
        instance.short_url = get_short_url(instance.url)
        instance.save()
        return instance
