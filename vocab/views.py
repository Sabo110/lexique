from django.shortcuts import render, redirect
from .models import Mot, Categorie
from .forms import MotForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MotSerializer


def liste_mots(request):
    mots = Mot.objects.select_related('categorie').all()

    return render(request, 'liste.html', {
        'mots': mots
    })

def recherche(request):
    q = request.GET.get('q')

    mots = Mot.objects.filter(
        terme__icontains=q
    )

    return render(request, 'liste.html', {
        'mots': mots
    })

def ajouter_mot(request):

    if request.method == "POST":
        form = MotForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("liste")

    else:
        form = MotForm()

    return render(
        request,
        "add.html",
        {
            "form": form
        }
    )


@api_view(['GET'])
def api_mots(request):

    mots = Mot.objects.all()

    serializer = MotSerializer(mots, many=True)

    return Response(serializer.data)
