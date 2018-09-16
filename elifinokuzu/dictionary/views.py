import random, json
from django.shortcuts import render, redirect
from dictionary.models import Node, Edge
from comments.models import Comment
from .forms import SubmissionForm, Search
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse

def search(request):
    form = Search()
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            searched_word = form.cleaned_data['search']
            nodes = Node.objects.filter(name__contains=searched_word)
            edges = Edge.objects.all()
            return render(request, 'search.html', {
                'form': form,
                "searched_word": nodes,
                'edges': edges,
            })

    return render(request, 'search.html',{"form" : form})

def home(request):
    user_list = Node.objects.all()
    user_list = user_list[::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 5)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    nodes = Node.objects.all()

    if len(Node.objects.all()) > 0:
        random_word = random.choice(Node.objects.all()).id
    else:
        random_word = "None"

    if request.method == "POST":    #Search bar
        form = Search(request.POST)
        if form.is_valid():
            searched_word = form.cleaned_data['search']
            nodes = Node.objects.filter(name__contains=searched_word)
            edges = Edge.objects.all()
            return render(request, 'search.html', {
                'form': form,
                "searched_word": nodes,
                'edges': edges,
            })

    return render(request, 'home.html', {
        'search': Search(),
        'title': 'Öküzün Elifi',
        'nodes': nodes,
        'random_word': random_word,
        'users': users,
        #'full_list_json': full_list_json,
    })


def node_detail(request, id):
    node = Node.objects.get(id=id)
    incoming = node.incoming.all()
    outgoing = node.outgoing.all()
    comments = Comment.objects.filter(model_id=node.model_id)
    return render(request, 'node_detail.html', {
        'node': node,
        'incoming': incoming,
        'outgoing': outgoing,
        'title': 'Öküzün Elifi: %s' % node.name,
        "comments": comments,
    })


def edge_detail(request, id):
    edge = Edge.objects.get(id=id)
    comments = Comment.objects.filter(model_id=edge.model_id)
    # import pdb
    # pdb.set_trace()
    return render(request, 'edge_detail.html', {
        'edge': edge,
        'edge.source': edge.source,
        'edge.destination': edge.destination,
        'edge.type_of_edge': edge.type_of_edge,
        'title': 'Öküzün Elifi: %s' % edge.type_of_edge,
        "comments": comments,
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
            if [i for i in Node.objects.all() if i.name == form.cleaned_data['source_node']] == [] \
                or [i for i in Node.objects.all() if i.name == form.cleaned_data['target_node']] == []:
                
                try:
                    source_node = Node.objects.get(name=form.cleaned_data['source_node'])
                except Node.DoesNotExist:
                    source_node = Node.objects.create(name=form.cleaned_data['source_node'],language=form.cleaned_data['source_language'],user=request.user, model_id=len(Node.objects.all()))

                try:
                    target_node = Node.objects.get(name=form.cleaned_data['target_node'])
                except Node.DoesNotExist:
                    target_node = Node.objects.create(name=form.cleaned_data['target_node'],language=form.cleaned_data['target_language'],user=request.user, model_id=len(Node.objects.all()))

                edge = Edge.objects.create(source=source_node,destination=target_node,is_directed=False,type_of_edge=form.cleaned_data['type_of_edge'],resource=form.cleaned_data['resource'],user=request.user, model_id=len(Edge.objects.all()))
            
            else:
                return render(request, 'submit.html',
                    {"error" : "there are already those nodes available, please try new one", 
                    'form': SubmissionForm()}
                    )

            return redirect(reverse("node_detail", args=[source_node.id]))
    return render(request, 'submit.html', {"form" : form})


def language(request, language):
    nodes = Node.objects.filter(language=language)
    return render(request, 'language.html',{
        "language": language,
        "nodes": nodes,
        })

def delete_own_created(request, own_id):
    try:
        own_id = Node.objects.get(id=own_id)
    except:
        own_id = Edge.objects.get(id=own_id)
        own_id.source.delete()
        own_id.destination.delete()

    own_id.delete()
    
    return redirect("/")