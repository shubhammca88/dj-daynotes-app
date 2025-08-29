from django.test import TestCase
from django.urls import reverse
from .models import Note

class NotebookTestCase(TestCase):
    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            body="This is a test note content."
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.body, "This is a test note content.")

    def test_dashboard_view(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_create_note_view(self):
        response = self.client.post(reverse('create_note'), {
            'title': 'New Test Note',
            'body': 'New test content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title='New Test Note').exists())