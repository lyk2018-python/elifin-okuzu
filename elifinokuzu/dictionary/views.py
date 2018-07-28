import random
from django.shortcuts import render, redirect
from dictionary.models import Node, Edge
from .forms import SubmissionForm,Search
from django.urls import reverse
from django.template import RequestContext
from django.http import HttpResponse



def home(request):
    nodes = Node.objects.all()

    if len(Node.objects.all()) > 0:
        random_word = random.choice(Node.objects.all()).id
    else:
        random_word = "None"

    return render(request, 'home.html', {
        'title': 'Öküzün Elifi',
        'nodes': nodes,
        'random_word': random_word,
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

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')

def submit(request):
    form = SubmissionForm()

    if request.method == "POST":
        form = SubmissionForm(request.POST)

        if form.is_valid():
            source_node = Node.objects.create(
                name=form.cleaned_data['source_node'],
                language=form.cleaned_data['source_language'],
            )
            target_node = Node.objects.create(
                name=form.cleaned_data['target_node'],
                language=form.cleaned_data['target_language'],
            )
            edge = Edge.objects.create(
                source=source_node,
                destination=target_node,
                is_directed=False,
                type_of_edge=form.cleaned_data['type_of_edge'],
                resource=form.cleaned_data['resource'],
            )

            return redirect(reverse("node_detail", args=[source_node.id]))
    else:
        return render(request, 'submit.html',{"form" : form})

def search(request):


    form = Search()
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            searched_word = form.cleaned_data['search']
            nodes = Node.objects.filter(name__contains=searched_word)
            edges = Edge.objects.all()
            return render(request, 'search.html', {
                'form':form,
                "searched_word": nodes,
                'edges': edges,
            })


                
    return render(request, 'search.html',{"form" : form})





