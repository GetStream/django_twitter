from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from stream_twitter import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve

# from allauth.account import urls as allauthurls

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^discover/', login_required(views.discover)),
    url(r'^timeline/',
        login_required(views.TimelineView.as_view())),
    url(r'^user/(?P<user_name>.+)/$', views.user),
    url(r'^hashtag/(?P<hashtag_name>.+)/', views.hashtag),
    url(r'^$', views.HomeView.as_view()),
    url(r'^follow/$', login_required(views.follow), name='follow'),
    url(r'^unfollow/(?P<target_id>\d+)/$', login_required(views.unfollow),
        name='unfollow'),
    url(r'^robots.txt$', TemplateView.as_view(
      template_name='stream_twitter/robots.txt',
      content_type="text/plain"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += [
    url(r'^media/(?P<path>.*)', serve,
        {'document_root': settings.MEDIA_ROOT})
]
