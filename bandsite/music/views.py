from django.shortcuts import render
from .models import BandMember

def home(request):
    members = BandMember.objects.all()
    return render(request, 'music/home.html', {'members': members})

