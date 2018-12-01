from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
import logging
from webapp.models import *

def info(msg):
    logger = logging.getLogger('command')
    logger.info(msg)

class ArtistListView(TemplateView):
    template_name = "artist_list.html"

    def get(self, request, *args, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)

        artists = Artist.objects.mongo_find()

        art = []
        for artist in artists[:10]:
            art.append(artist)

        d = { 'objects' : art }

        #info(art[:10])

        context['artists'] = artists
        info(context['artists'])

        return render(self.request, self.template_name, d)
