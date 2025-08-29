from django.core.management.base import BaseCommand
from daynotes.models import Note

class Command(BaseCommand):
    help = 'Create demo note'

    def handle(self, *args, **options):
        note, created = Note.objects.get_or_create(
            title='Welcome to Daynotes App',
            defaults={'body': 'This is your first note! You can create, edit, and delete notes using this application. The interface is clean and user-friendly.\n\nFeatures:\n- Create new notes\n- Edit existing notes\n- Delete notes\n- Responsive design\n\nGet started by creating your own notes!'}
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Demo note created!'))
        else:
            self.stdout.write(self.style.WARNING('Demo note already exists'))