from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Item

class ItemAPITest(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpass')

       
        self.token = self.get_jwt_token()

    def get_jwt_token(self):
        
        url = reverse('login')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'}, format='json')
        return response.data['access']

    def auth_headers(self):
        
        return {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
    def test_create_item(self):
        url = reverse('item_create')  
        data = {
            'name': 'Test Item',
            'description': 'Test Description'
        }
        
        
        response = self.client.post(url, data, format='json', **self.auth_headers())
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    