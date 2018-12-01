from django.contrib import admin
from django.urls import path
import webapp.views as webapp_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artist_list/', webapp_view.ArtistListView.as_view())
]
