from django.core.management.base import BaseCommand
from django.core.management import call_command
from stream_twitter.models import Tweet


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command('migrate', interactive=False)
        call_command('loaddata', './pytutorial/fixtures/initial_data.json')

        for tweet in Tweet.objects.all():
            tweet.delete()
            tweet.save()
