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
    for i in edges:
        if {'name': '{}'.format(i.source.name)} not in tuple(liste['nodes']):
            liste['nodes'].append({'name':'{}'.format(i.source.name)})

    for i in edges:
        if {'name': '{}'.format(i.destination.name)} not in tuple(liste['nodes']):
            liste['nodes'].append({'name':'{}'.format(i.destination.name)})

    for i in edges:
        for j in range(len(liste['nodes'])):
            if i.source.name == liste['nodes'][j]['name']:
                    try:
                        liste['links'].append({'source':tuple(liste['nodes']).index({'name':'{}'.format(i.source.name)}),\
                         'target':tuple(liste['nodes']).index({'name':'{}'.format(i.destination.name)})})
                    except:
                        pass

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