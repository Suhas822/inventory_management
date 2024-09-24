from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Item

class ItemAPITest(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Obtain the JWT token for the test user
        self.token = self.get_jwt_token()

    def get_jwt_token(self):
        # Get JWT token for authentication
        url = reverse('login')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        return response.data['access']

    def auth_headers(self):
        # Return headers including the JWT token
        return {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
    def test_create_item(self):
        url = reverse('item_create')  # Change to the actual URL name for creating an item
        data = {
            'name': 'Test Item',
            'description': 'Test Description'
        }
        
        # Make the POST request with authentication headers
        response = self.client.post(url, data, format='json', **self.auth_headers())
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    