from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from events.models import Event, Interest
from django.utils import timezone

User = get_user_model()

class EventViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.interest = Interest.objects.create(
            name='Test Interest',
            description='Test Description'
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='Test Description',
            date=timezone.now(),
            location='Test Location',
            creator=self.user,
            max_participants=10
        )
        self.event.interests.add(self.interest)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/home.html')

    def test_event_list_view(self):
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_list.html')
        self.assertContains(response, 'Test Event')

    def test_event_detail_view(self):
        response = self.client.get(reverse('event_detail', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_detail.html')
        self.assertContains(response, 'Test Event') 