from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
import logging
from webapp.models import *

def info(msg):
    logger = logging.getLogger('command')
    logger.info(msg)

class ArtistListView(TemplateView):
    template_name = "artist_list.html"

    def search(self,item = '',content = '',limit = 100):
        if content == '':
            artists = Artist.objects.mongo_find()
        else:
            if item == 'name':
                artists = Artist.objects.mongo_find({'name':content})
            elif item == 'aliase':
                artists = Artist.objects.mongo_find({'aliases.name':content})
            elif item == 'tag':
                artists = Artist.objects.mongo_find({'tags.value':content})
            limit = artists.count()
        arts = []

        # 100件にしている。全体で921337件あるので表示に時間がかかりすぎる為
        for artist in artists[:limit]:
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
                begin_date = []
                if 'year' in artist['begin']:
                    begin_date.append(str(artist['begin']['year']))
                if 'month' in artist['begin']:
                    begin_date.append(str(artist['begin']['month']))
                if 'date' in artist['begin']:
                    begin_date.append(str(artist['begin']['date']))
                art['begin'] = '/'.join(begin_date)

            # 活動終了日の整形
            if 'end' in artist:
                end_date = []
                if 'year' in artist['end']:
                    end_date.append(str(artist['end']['year']))
                if 'month' in artist['end']:
                    end_date.append(str(artist['end']['month']))
                if 'date' in artist['end']:
                    end_date.append(str(artist['end']['date']))
                art['end'] = '/'.join(end_date)

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

        return render(self.request, self.template_name, d)

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            if 'search' in request.GET:
                info(request.GET['search'])
                info(request.GET['search_item'])
                return self.search(request.GET['search_item'], request.GET['search'])
            else:
                return self.search()
