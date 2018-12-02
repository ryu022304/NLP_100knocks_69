from django.contrib import admin
from django.urls import path
import webapp.views as webapp_view
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artist_list/', webapp_view.ArtistListView.as_view()),
    path('artist_list/search',webapp_view.ArtistListView, name='getSearchResult')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
