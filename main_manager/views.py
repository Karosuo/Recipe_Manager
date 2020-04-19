from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from main_manager.utils import process_recipe_file, process_plan_file, process_inventory_file


def shopping_list(request):
    return render(request, 'main_manager/shopping_list.html', None)


def load_data_page_render(request):
    return render(request, 'main_manager/load_data.html', None)


def process_load_files(request):
    """
    Only process one file at a time, the one in the 0th position of the request.FILES list
    :param request:
    :return:
    """
    json_return = {"BaseResponse": "Not a POST request"}
    json_return["LoadedFiles"] = False

    if request.method == "POST":
        key_list = []

        for c_key in request.FILES.keys():
            key_list.append(c_key)

        if len(key_list) > 0:
            ref_flag = key_list[0]
            if ref_flag == "recipes_file":
                process_recipe_file(request.FILES[ref_flag])
            elif ref_flag == "plan_file":
                process_plan_file(request.FILES[ref_flag])
            elif ref_flag == "inventory_file":
                process_inventory_file(request.FILES[ref_flag])

        # Detect which file it is by the flag name
        # Check if all format is ok, if not, answer format is not ok
        # Each loop that checks format, saves the values into an array
        # Use the array to save the elements on DB
        json_return["BaseResponse"] = "Correctly processed data files"
        json_return["LoadedFiles"] = True

    return JsonResponse(json_return)


def main_redirection(request):

    return HttpResponseRedirect(reverse('shopping_list_url'))
