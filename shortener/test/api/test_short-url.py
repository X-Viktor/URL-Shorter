import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_url_create(api_client):
    """Добавление ссылки."""
    url = reverse('shorturl-list')
    url_data = {'url': 'https://www.google.com/'}
    response = api_client.post(url, data=url_data)

    assert response.data['url'] == url_data['url']
    assert response.data['short_url'] != ''
    assert response.status_code == 201


def test_url_edit(api_client, short_url):
    """Редактирование ссылки."""
    url = reverse('shorturl-detail', kwargs={'pk': short_url.pk})
    url_data = {'url': 'https://yandex.ru'}
    response = api_client.put(url, data=url_data)

    assert response.data['url'] == url_data['url']
    assert response.data['short_url'] != short_url.short_url
    assert response.status_code == 200


def test_url_delete(api_client, short_url):
    """Удаление ссылки."""
    url = reverse('shorturl-detail', kwargs={'pk': short_url.pk})
    response = api_client.delete(url)

    assert response.status_code == 204


def test_url_detail(api_client, short_url):
    """Получение подробностей ссылки."""
    url = reverse('shorturl-detail', kwargs={'pk': short_url.pk})
    response = api_client.get(url)

    assert response.data['url'] == short_url.url
    assert response.status_code == 200


def test_url_list(api_client):
    """Получение всех ссылок."""
    url = reverse('shorturl-list')
    response = api_client.get(url)

    assert response.status_code == 200
