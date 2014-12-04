from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from stream_twitter import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tweet/', login_required(views.TweetView.as_view())),
    url(r'^follow/', login_required(views.FollowView.as_view())),
)
