from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.views.static import serve

from stream_twitter import views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('discover/', login_required(views.DiscoverView.as_view()), name='discover'),
    path('timeline/',
        login_required(views.TimelineView.as_view()), name='timeline_feed'),
    re_path(r'^user/(?P<username>.+)/', views.UserView.as_view(), name='user_feed'),

    re_path(r'^hashtag/(?P<hashtag>.+)/', views.HashtagView.as_view(), name='hashtag_feed'),
    path('', views.HomeView.as_view()),
    path('follow/', login_required(views.FollowView.as_view()), name='follow'),
    re_path(r'^unfollow/(?P<target_id>\d+)/', login_required(views.UnfollowView.as_view()),
        name='unfollow'),
    path('robots.txt', TemplateView.as_view(
      template_name='stream_twitter/robots.txt',
      content_type="text/plain"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    re_path('^media/(?P<path>.*)', serve,
        {'document_root': settings.MEDIA_ROOT})
]
