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
        #context = super(ArtistListView, self).get_context_data(**kwargs)

        artists = Artist.objects.mongo_find()

        arts = []
        for artist in artists[:100]:
            art = artist

            # 別名の整形
            if 'aliases' in artist:
                aliase_name = []
                for aliase in artist['aliases']:
                    aliase_name.append(aliase['name'])
                art['aliases'] = ',\n'.join(aliase_name)
                #art['aliases'] = aliase_name

            # 活動開始日の整形
            if 'begin' in artist:
                begin_date = str(artist['begin']['year'])
                if 'month' in artist['begin']:
                    begin_date += '/'+ str(artist['begin']['month'])
                    if 'date' in artist['begin']:
                        begin_date += '/'+ str(artist['begin']['date'])
                art['begin'] = begin_date

            # 活動終了日の整形
            if 'end' in artist:
                end_date = str(artist['end']['year'])
                if 'month' in artist['end']:
                    end_date += '/'+ str(artist['end']['month'])
                    if 'date' in artist['end']:
                        end_date += '/'+ str(artist['end']['date'])
                art['end'] = end_date

            # タグの整形
            if 'tags' in artist:
                tag_contents = []
                for tag in artist['tags']:
                    tag_contents.append(tag['value']+':'+ str(tag['count']))
                art['tags'] = ',\n'.join(tag_contents)

            # レーティングの整形
            if 'rating' in artist:
                art['rating_num'] = str(artist['rating']['count'])
                art['rating_ave'] = str(artist['rating']['value'])

            arts.append(art)

        d = { 'objects' : arts }

        #info(art[:10])

        #context['artists'] = artists
        #info(context['artists'])

        return render(self.request, self.template_name, d)
