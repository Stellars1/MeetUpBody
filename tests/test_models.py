from django.test import TestCase
from django.contrib.auth import get_user_model
from events.models import Event, Interest
from django.utils import timezone

User = get_user_model()

class EventModelTest(TestCase):
    def setUp(self):
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

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.creator, self.user)
        self.assertEqual(self.event.interests.count(), 1)

    def test_event_participants(self):
        self.event.participants.add(self.user)
        self.assertEqual(self.event.participants.count(), 1)
        self.assertTrue(self.user in self.event.participants.all()) 