from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import State
from django.urls import reverse

class StateAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.state_data = {'name': 'Inge Jei New'}
        self.state = State.objects.create(name='Inge Jei New')
        self.url = reverse('state-list')

    def test_get_states(self):
    
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Inge Jei New')

    def test_create_state(self):
    
        response = self.client.post(self.url, self.state_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(State.objects.count(), 2)
        self.assertEqual(State.objects.last().name, 'Inge Jei New')

    # def test_update_state(self):
      
    #     update_url = reverse('state-detail', kwargs={'pk': self.state.id})
    #     response = self.client.put(update_url, {'name': 'Jei Update'}, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.state.refresh_from_db()
    #     self.assertEqual(self.state.name, 'Jei Update')

    # def test_delete_state(self):
       
    #     delete_url = reverse('state-detail', kwargs={'pk': self.state.id})
    #     response = self.client.delete(delete_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(State.objects.count(), 0)
