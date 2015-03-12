from django.core.management.base import BaseCommand
from django.core.management import call_command
from stream_twitter.models import Tweet
from stream_django.feed_manager import feed_manager


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        call_command('migrate', interactive=False)
        call_command('loaddata', './pytutorial/fixtures/initial_data.json')

        #make sure we send data to Stream
        feed_manager.enable_model_tracking()

        for tweet in Tweet.objects.all():
            tweet.delete()
            tweet.save()
