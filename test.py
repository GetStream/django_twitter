from django.contrib.auth.models import User
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

enricher = Enrich()
feed = feed_manager.get_user_feed(1)
activities = feed.get(limit=25)['results']
enricher.enrich_activities(activities)
for i in activities:
    print(i)
    print("\n########\n")