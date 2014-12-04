from django.views.generic.edit import CreateView
from stream_twitter.models import Follow
from stream_twitter.models import Tweet


class TweetView(CreateView):
    model = Tweet
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tweet, self).form_valid(form)


class FollowView(CreateView):
    model = Follow
    fields = ['target']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tweet, self).form_valid(form)
