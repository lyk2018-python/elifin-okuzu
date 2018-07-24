from django.shortcuts import render
from dictionary.models import Node

def home(request):
    nodes = Node.objects.all()

    return render(request, 'home.html', {
        'title': 'Öküzün Elifi',
        'nodes': nodes,
    })

def node_detail(request, id):
    node = Node.objects.get(id=id)
    incoming = node.incoming.all()
    outgoing = node.outgoing.all()
    return render(request, 'node_detail.html', {
        'node': node,
        'incoming': incoming,
        'outgoing': outgoing,
        'title': 'Öküzün Elifi: %s' % node.name,
    })
