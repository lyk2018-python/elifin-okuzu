import json
from django.shortcuts import render, redirect
from reports.forms import ReportForm
from django.urls import reverse
from django.http import HttpResponse
from dictionary.models import Node, Edge


def reportdone(request):
    return render(request, "reports/reportdone.html")

def jsondata(request):
    nodes = Node.objects.all()
    edges = Edge.objects.all()
    liste = {}
    liste['nodes'] = []
    liste['links'] = []
    #liste["nodes"] = list(map(lambda x,y: dict({x:y}), ["name" for i in range(len(nodes))], [i.name for i in nodes]))
    #liste["edges"] = list(map(lambda x,y: dict({x:y}), [i.source.name for i in edges], [i.resource for i in edges]))
    #liste["links"] = list(map(lambda x,y,i,j: dict({x:y, i:j}), ["source" for i in range(len(edges))], [i.resource for i in edges],["target" for i in range(len(edges))], [i.source.name for i in edges]))
    liste["nodes"] = list(map(lambda x,y: dict({x:y}), ["name" for i in range(len(edges) * 2)],[i.source.name for i in edges] + [i.destination.name for i in edges]))
    #Edge.objects.filter(source=Node.objects.all()[0])[0].resource




    for i in edges:
        for j in range(len(liste['nodes'])):
                if i.source.name == liste['nodes'][j]['name']:
                        try:
                            liste['links'].append({'source':tuple(liste['nodes']).index({'name':'{}'.format(i.source.name)}), 'target':tuple(liste['nodes']).index({'name':'{}'.format(i.destination.name)})})
                        except:
                            pass
    
    # full_list = {}
    #liste['links'].append({'source': tuple(liste['edges']).index({'name':'{}'.format(i.resource)})}, {'target':tuple(liste['edges']).index({'name':''.format(i.source.name)})})
    # for i in nodes:
    #     full_list[i.model_id] = i.name

    # fl = open("full_list.json", "r")
    # json.load(fl)

    # full_list_json = json.dumps(full_list, ensure_ascii=False).encode('utf8')
    # to_json = open("full_list.json", "w")
    # to_json.write(str(full_list_json))
    # to_json.close()
    a = {
        "nodes": [
        { "name": "raar"},
        { "name": "mirkan"},
        { "name": "babam"},
        { "name": "anam"},
        { "name": "avrat"},
        { "name": "Ar ˁawrāt"},
        { "name": "sakat"},
        { "name": "Ar saḳaṭ"},
        { "name": "baba"},
        { "name": "çoc ba-ba"},
        { "name": "sev"},
        { "name": "Fa şēb/şīb"},
        { "name": "sevda"},
        { "name": "Ar sawdāˀ"},
        { "name": "Yunus"},
        { "name": "Dolphin"}],
        "links": [{
            "source": 0,
            "target": 1
        },{
            "source": 0,
            "target": 2
        },{
            "source": 0,
            "target": 3
        },{
            "source": 0,
            "target": 4
        },{
            "source": 1,
            "target": 2
        },{
            "source": 1,
            "target": 3
        },{
            "source": 1,
            "target": 4
        },{
            "source": 2,
            "target": 3
        },{
            "source": 2,
            "target": 4
        },{
            "source": 0,
            "target": 5
        },{
            "source": 5,
            "target": 6
        },{
            "source": 5,
            "target": 7
        },{
            "source": 0,
            "target": 8
        },{
            "source": 0,
            "target": 9
        },{
            "source": 0,
            "target": 10
        },{
            "source": 8,
            "target": 7
        }]}
    print(a)
    print(liste)
    return HttpResponse(json.dumps(liste, ensure_ascii=False).encode('utf8'))

def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect(reverse("reportdone"))
    else:
        form = ReportForm()
    return render(request, 'reports/report.html', {'form': form})