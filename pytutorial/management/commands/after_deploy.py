from django.core.management.base import BaseCommand
from stream_twitter.models import Follow
from django.contrib.auth import get_user_model
from django.core.management import call_command


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command('syncdb', interactive=False)
        call_command('migrate', interactive=False)
        call_command('loaddata', './pytutorial/fixtures/initial_data.json')
        # admin = get_user_model().objects.get(username="admin")
        # Follow.objects.create(user=admin, target=admin)
