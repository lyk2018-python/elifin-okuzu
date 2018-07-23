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

	return render(request, 'note_detail.html', {
		'title': 'Öküzün Elifi: {}'.format(node.name),
		'node': node,
	})
