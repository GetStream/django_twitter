from django import forms
from stream_twitter.models import Follow, Tweet


class FollowForm(forms.ModelForm):

    class Meta:
        exclude = set()
        model = Follow
