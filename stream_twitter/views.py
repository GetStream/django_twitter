from django.views.generic.edit import CreateView
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, get_user_model, \
    login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext

from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

from stream_twitter.models import Follow
from stream_twitter.models import Tweet, Hashtag
# from stream_twitter.forms import TweetForm, HashtagForm

from pytutorial import settings


class TweetView(CreateView):
    model = Tweet
    fields = ['text']
    success_url="/timeline/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetView, self).form_valid(form)


class FollowView(CreateView):
    model = Follow
    fields = ['target']
    success_url = "/timeline/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FollowView, self).form_valid(form)

class HomeView(CreateView):
    greeting = "Welcome to Stream Twitter"

    def get(self, request):
        context = RequestContext(request)
        context_dict = {}
        context_dict['greeting'] = self.greeting
        context_dict['user'] = request.user
        return render_to_response('stream_twitter/home.html', context_dict, context)

@login_required
def timeline(request):
    enricher = Enrich()
    feeds = feed_manager.get_news_feeds(request.user.id)
    activities = feeds.get('flat').get()[u'results']
    enricher.enrich_activities(activities)
    context = {
        'activities': activities
    }
    return render(request, 'stream_twitter/timeline.html', context)

def user(request, user_name):
    enricher = Enrich()
    user = get_object_or_404(User ,username=user_name)
    feeds = feed_manager.get_user_feed(user.id)
    activities = feeds.get()[u'results']
    enricher.enrich_activities(activities)
    context = {
        'activities': activities,
        'user': user
    }
    return render(request, 'stream_twitter/user.html', context)


def hashtag(request, hashtag_name):
    enricher = Enrich()

    hashtag_name = hashtag_name.lower()
    feed = feed_manager.get_feed('hashtag', hashtag_name);
    activities = feed.get(limit=25)['results']

    enricher.enrich_activities(activities)
    context = {
        'activities': activities
    }
    return render(request, 'stream_twitter/hashtag.html', context)

def trending_hashtags(request):
    hashtags = Hashtag.objects.order_by('-occurrences')
    context = {
        'hashtags': hashtags
    }
    return render(request, 'stream_twitter/all_hashtags.html', context)

def recent_users(request):
    users = User.objects.order_by('-used_amount')
    context = {
        'users': users
    }
    return render(request, 'stream_twitter/all_users.html', context)
