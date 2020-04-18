from django.shortcuts import render

# Create your views here.
def shopping_list(request):

    return render(request, 'main_manager/shopping_list.html', None)

