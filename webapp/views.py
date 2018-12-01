from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from webapp.models import *


class ArtistListView(TemplateView):
    template_name = "artist_list.html"

    def get(self, request, *args, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
