import pytest
from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def short_url(api_client):
    """Ссылка."""
    return mixer.blend('shortener.ShortURL')
