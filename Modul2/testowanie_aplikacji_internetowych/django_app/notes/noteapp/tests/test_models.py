from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from noteapp.models import Tag, Note

'''
Uruchomienie testów:
$ python manage.py test noteapp.tests.test_models
python manage.py test noteapp.tests
'''

class ModelsTestCase(TestCase):

    def setUp(self):
        # Tworzenie użytkownika
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Tworzenie kilku tagów
        self.tag1 = Tag.objects.create(name='Tag1', user=self.user)
        self.tag2 = Tag.objects.create(name='Tag2', user=self.user)

        # Tworzenie notatki
        self.note = Note.objects.create(
            name='Test Note',
            description='To jest testowa notatka.',
            user=self.user
        )
        self.note.tags.add(self.tag1, self.tag2)

    def test_tag_creation(self):
        """Testuje poprawność tworzenia tagów."""
        tag = Tag.objects.get(name='Tag1')
        self.assertEqual(tag.name, 'Tag1')
        self.assertEqual(tag.user.username, 'testuser')
        self.assertEqual(str(tag), 'Tag1')

    def test_note_creation(self):
        """Testuje poprawność tworzenia notatki."""
        note = Note.objects.get(name='Test Note')
        self.assertEqual(note.name, 'Test Note')
        self.assertEqual(note.description, 'To jest testowa notatka.')
        self.assertFalse(note.done)
        self.assertEqual(note.user.username, 'testuser')
        self.assertEqual(str(note), 'Test Note')

    def test_note_tags(self):
        """Testuje, czy notatka ma poprawne tagi."""
        note = Note.objects.get(name='Test Note')
        tags = note.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(self.tag1, tags)
        self.assertIn(self.tag2, tags)

    def test_unique_tag_constraint(self):
        """Testuje unikalne ograniczenie dla Tag."""
        with transaction.atomic():
            # Próba utworzenia tagu o tej samej nazwie dla tego samego użytkownika powinna podnieść wyjątek IntegrityError
            with self.assertRaises(IntegrityError):
                Tag.objects.create(name='Tag1', user=self.user)

    def test_note_str_method(self):
        """Testuje metodę __str__ klasy Note."""
        note = Note.objects.get(name='Test Note')
        self.assertEqual(str(note), 'Test Note')

    def test_tag_str_method(self):
        """Testuje metodę __str__ klasy Tag."""
        tag = Tag.objects.get(name='Tag1')
        self.assertEqual(str(tag), 'Tag1')
