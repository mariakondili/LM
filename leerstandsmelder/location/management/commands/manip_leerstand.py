from django.core.management.base import BaseCommand
from leerstandsmelder.location.models import Location 

class Command(BaseCommand):
    help = "a command"

    def handle(self, *args, **options):
        print(Location.objects.all().count())
