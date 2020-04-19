from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def shopping_list(request):
    return render(request, 'main_manager/shopping_list.html', None)


def main_redirection(request):

    return HttpResponseRedirect(reverse('shopping_list_url'))
