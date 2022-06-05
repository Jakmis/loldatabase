
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from loldb.models import Champion, Region
# Create your views here.

def index(request):

    num_champions = Champion.objects.all().count()

    champions = Champion.objects.order_by('name')[:3]

    regions = Region.objects.all()

    context = {
            'num_champions': num_champions,
            'champions': champions,
            'regions':regions,
    }

    return render(request, 'index.html', context=context)

class ChampionListView(ListView):
    model = Champion

    context_object_name = 'champions'

    template_name = 'list.html'

class ChampionDetailView(DetailView):
    model = Champion

    context_object_name = 'champions_detail'

    template_name = 'detail.html'