import pytest
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_unauthenticated_user_cannot_create_task():
    payload = {
    "title": "",
    "description": "",
    "status": "TODO",
    "priority": "MEDIUM"
}
    client = APIClient()
    url = reverse('task-list')
    response = client.post(url, data=payload)
    assert response.status_code == 403


@pytest.mark.django_db
def test_authenticated_user_can_create_task():
    payload = {
    "title": "Title test",
    "description": "Desc test",
    "status": "TODO",
    "priority": "MEDIUM"
}
    user = User.objects.create_user(username='test', password='test1234')
    client = APIClient()
    client.force_authenticate(user=user)

    url = reverse('task-list')
    response = client.post(url, data=payload)

    assert response.data['title'] == 'Title test'
    assert response.status_code == 201