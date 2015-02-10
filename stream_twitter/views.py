from django.views.generic.edit import CreateView
from django.shortcuts import render_to_response, render
from django.template.response import TemplateResponse

from django.contrib.auth.decorators import login_required


from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

from stream_twitter.models import Follow
from stream_twitter.models import Tweet


class TweetView(CreateView):
    model = Tweet
    fields = ['text']
    success_url="/timeline/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetView, self).form_valid(form) # There is a bug here


class FollowView(CreateView):
    model = Follow
    fields = ['target']
    success_url = "/timeline/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FollowView, self).form_valid(form) # There is a bug here

class HomeView(CreateView):
    greeting = "Welcome to Stream Twitter"

    def get(self, request):
        return render_to_response('stream_twitter/home.html', {'greeting': self.greeting})

@login_required
def timeline(request):
    enricher = Enrich()
    user = feed_manager.get_user_feed(request.user.id)
    activities = user.get(limit=25)[u'results']
    enricher.enrich_activities(activities)
    context = {
        'activities': activities
    }
    return render(request, 'stream_twitter/timeline.html', context)