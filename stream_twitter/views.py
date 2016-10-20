from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager
from stream_twitter.forms import FollowForm
from stream_twitter.models import Follow
from stream_twitter.models import Tweet, Hashtag
from pytutorial import settings


enricher = Enrich()


class TimelineView(CreateView):
    model = Tweet
    fields = ['text']
    success_url = "/timeline/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TimelineView, self).form_valid(form)

    def get(self, request):
        feeds = feed_manager.get_news_feeds(request.user.id)
        activities = feeds.get('timeline').get()['results']
        activities = enricher.enrich_activities(activities)
        hashtags = Hashtag.objects.order_by('-occurrences')
        context = {
            'activities': activities,
            'form': self.get_form_class(),
            'login_user': request.user,
            'hashtags': hashtags
        }
        return render(request, 'stream_twitter/timeline.html', context)


class HomeView(CreateView):
    greeting = "Welcome to Stream Twitter"

    def get(self, request):
        if not request.user.is_authenticated() and not settings.USE_AUTH:
            admin_user = authenticate(
                username=settings.DEMO_USERNAME, password=settings.DEMO_PASSWORD)
            auth_login(request, admin_user)
        context = {
            'greeting': self.greeting,
            'login_user': request.user,
            'users': User.objects.order_by('date_joined')[:50]
        }
        return render(request, 'stream_twitter/home.html', context)


def follow(request):
    form = FollowForm(request.POST)
    if form.is_valid():
        follow = form.instance
        follow.user = request.user
        follow.save()
    return redirect("/timeline/")


def unfollow(request, target_id):
    follow = Follow.objects.filter(user=request.user, target_id=target_id).first()
    if follow is not None:
        follow.delete()
    return redirect("/timeline/")


def discover(request):
    users = User.objects.order_by('date_joined')[:50]
    login_user = User.objects.get(username=request.user)
    following = []
    for i in users:
        if len(i.followers.filter(user=login_user.id)) == 0:
            following.append((i, False))
        else:
            following.append((i, True))
    login_user = User.objects.get(username=request.user)
    context = {
        'users': users,
        'form': FollowForm(),
        'login_user': request.user,
        'following': following
    }
    return render(request, 'stream_twitter/follow_form.html', context)


def user(request, user_name):
    user = get_object_or_404(User, username=user_name)
    feeds = feed_manager.get_user_feed(user.id)
    activities = feeds.get()['results']
    activities = enricher.enrich_activities(activities)
    context = {
        'activities': activities,
        'user': user,
        'login_user': request.user
    }
    return render(request, 'stream_twitter/user.html', context)


def hashtag(request, hashtag_name):
    hashtag_name = hashtag_name.lower()
    feed = feed_manager.get_feed('user', 'hash_%s' % hashtag_name)
    activities = feed.get(limit=25)['results']

    activities = enricher.enrich_activities(activities)
    context = {
        'hashtag_name': hashtag_name,
        'activities': activities
    }
    return render(request, 'stream_twitter/hashtag.html', context)
