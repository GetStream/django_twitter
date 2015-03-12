from django.forms import ModelForm
from stream_twitter.models import Follow


class FollowForm(ModelForm):

    class Meta:
        model = Follow
