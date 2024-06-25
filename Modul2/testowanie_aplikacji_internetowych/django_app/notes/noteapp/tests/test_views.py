from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from noteapp.models import Note, Tag
from noteapp.forms import TagForm, NoteForm


'''
Uruchomienie testów:
$ python manage.py test noteapp.tests.test_views
python manage.py test noteapp.tests
'''


class ViewsTestCase(TestCase):

    def setUp(self):
        # Tworzenie klienta do symulacji żądań
        self.client = Client()
        # Tworzenie użytkownika
        self.user = User.objects.create_user(username='testuser', password='12345')
        # Logowanie użytkownika
        self.client.login(username='testuser', password='12345')

        # Tworzenie tagów i notatek
        self.tag = Tag.objects.create(name='Tag1', user=self.user)
        self.note = Note.objects.create(
            name='Test Note',
            description='To jest testowa notatka.',
            user=self.user
        )
        self.note.tags.add(self.tag)

    def test_main_view_authenticated(self):
        """Test widoku głównego dla zalogowanego użytkownika."""
        response = self.client.get(reverse('noteapp:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/index.html')
        self.assertContains(response, 'Test Note')

    def test_main_view_unauthenticated(self):
        """Test widoku głównego dla niezalogowanego użytkownika."""
        self.client.logout()
        response = self.client.get(reverse('noteapp:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/index.html')
        self.assertNotContains(response, 'Test Note')

    def test_tag_view_get(self):
        """Test widoku tagów przy użyciu metody GET."""
        response = self.client.get(reverse('noteapp:tag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/tag.html')
        self.assertIsInstance(response.context['form'], TagForm)

    def test_tag_view_post_valid(self):
        """Test widoku tagów przy użyciu metody POST z poprawnymi danymi."""
        response = self.client.post(reverse('noteapp:tag'), {'name': 'Tag2'})
        self.assertEqual(response.status_code, 302)  # Przekierowanie po zapisaniu
        self.assertTrue(Tag.objects.filter(name='Tag2', user=self.user).exists())

    def test_tag_view_post_invalid(self):
        """Test widoku tagów przy użyciu metody POST z niepoprawnymi danymi."""
        response = self.client.post(reverse('noteapp:tag'), {'name': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/tag.html')
        self.assertFalse(Tag.objects.filter(name='', user=self.user).exists())

    def test_note_view_get(self):
        """Test widoku notatek przy użyciu metody GET."""
        response = self.client.get(reverse('noteapp:note'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/note.html')
        self.assertIsInstance(response.context['form'], NoteForm)
        self.assertIn(self.tag, response.context['tags'])

    def test_note_view_post_valid(self):
        """Test widoku notatek przy użyciu metody POST z poprawnymi danymi."""
        response = self.client.post(reverse('noteapp:note'), {'name': 'New Note', 'description': 'New Description', 'tags': [self.tag.id]})
        self.assertEqual(response.status_code, 302)  # Przekierowanie po zapisaniu
        self.assertTrue(Note.objects.filter(name='New Note', user=self.user).exists())

    def test_note_view_post_invalid(self):
        """Test widoku notatek przy użyciu metody POST z niepoprawnymi danymi."""
        response = self.client.post(reverse('noteapp:note'), {'name': '', 'description': 'New Description'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/note.html')
        self.assertFalse(Note.objects.filter(description='New Description', user=self.user).exists())

    def test_detail_view(self):
        """Test widoku szczegółowego notatki."""
        response = self.client.get(reverse('noteapp:detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'noteapp/detail.html')
        self.assertEqual(response.context['note'], self.note)

    def test_set_done_view(self):
        """Test ustawiania notatki jako ukończonej."""
        response = self.client.post(reverse('noteapp:set_done', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Przekierowanie po aktualizacji
        self.note.refresh_from_db()
        self.assertTrue(self.note.done)

    def test_delete_note_view(self):
        """Test usuwania notatki."""
        response = self.client.post(reverse('noteapp:delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)  # Przekierowanie po usunięciu
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
