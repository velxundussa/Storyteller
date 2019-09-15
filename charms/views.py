from django.shortcuts import render

from charms.models import Charm


# Create your views here.
def list_charms(request):
    charms = Charm.objects.all()

    context = {
        'charms': charms
    }

    return render(request, 'charms/list.djhtml', context)

def details(request, charm_id):
    charm = Charm.objects.get(id=charm_id)

    context = {
        'charm': charm,
    }

    return render(request, 'charms/details.djhtml', context)
