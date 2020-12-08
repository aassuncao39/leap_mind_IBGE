import datetime
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.urls import reverse

from .forms import GeeksForm
from .models import Datas



def home_view(request):
    context = {}
    return render(request, "historico_pesquisa.html", context)


def get(request):
    form = GeeksForm
    context = {}
    context['form'] = GeeksForm()
    return render(request, "date.html", context)


def post(self, request):
    form = GeeksForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['post']
        text.save()
    return render(request, "date.html", args)