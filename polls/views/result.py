from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from ..models import Choice, Question

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
