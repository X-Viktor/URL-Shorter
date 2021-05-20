from rest_framework.viewsets import ModelViewSet

from shortener.api.serializers import ShortURLSerializer
from shortener.models import ShortURL


class ShortURLViewSet(ModelViewSet):
    """Операции с ссылками."""
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
