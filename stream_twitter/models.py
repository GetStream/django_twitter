from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from stream_django import activity
from stream_django.feed_manager import feed_manager


class Tweet(activity.Activity, models.Model):
    user = models.ForeignKey('auth.User')
    text = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def activity_object_attr(self):
        return self

    def parse_hashtags(self):
        return [slugify(i) for i in self.text.split() if i.startswith("#")]

    def parse_mentions(self):
        mentions = [slugify(i) for i in self.text.split() if i.startswith("@")]
        return User.objects.filter(username__in=mentions)

    @property
    def activity_notify(self):
        targets = []
        for hashtag in self.parse_hashtags():
            targets.append(feed_manager.get_feed('hashtag', hashtag))
        for user in self.parse_mentions():
            targets.append(feed_manager.get_news_feeds(user.id)['flat'])
        return targets


class Follow(models.Model):
    user = models.ForeignKey('auth.User', related_name='friends')
    target = models.ForeignKey('auth.User', related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'target')


def unfollow_feed(sender, instance, **kwargs):
    feed_manager.unfollow_user(instance.user_id, instance.target_id)


def follow_feed(sender, instance, created, **kwargs):
    if created:
        feed_manager.follow_user(instance.user_id, instance.target_id)


signals.post_delete.connect(unfollow_feed, sender=Follow)
signals.post_save.connect(follow_feed, sender=Follow)
