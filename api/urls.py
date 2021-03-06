from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'

urlpatterns = [
    url(r'^v1/artigo/', views.EntryDetail.as_view(), name='api_article'),
    url(r'^v1/comment/$', views.CommentDetail.as_view(), name='api_comments'),
    url(r'^v1/comment_page/$', views.CommentPageDetail.as_view(), name='api_comment_page'),
    url(r'^v1/vote/$', views.VoteDetail.as_view(), name='api_vote'),
    url(r'^v1/points/$', views.PointsDetail.as_view(), name='api_points'),
    url(r'^v1/trending/$', views.TrendingDetail.as_view(), name='api_trending'),
    url(r'^v1/search/$', views.SearchDetail.as_view(), name='api_search'),
    url(r'^v1/preview/$', views.PreviewDetail.as_view(), name='api_preview'),
]