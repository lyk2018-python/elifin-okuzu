from django.shortcuts import render, redirect
from support.forms import SupportForm
from django.urls import reverse


def supportdone(request):
    return render(request, "supports/supportdone.html")

def support(request):
    if request.method == "POST":
        form = SupportForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect(reverse("supportdone"))
    else:
        form = SupportForm()
    return render(request, 'supports/support.html', {'form': form})
