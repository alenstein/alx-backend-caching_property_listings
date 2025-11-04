from django.http import JsonResponse
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()
    data = list(properties.values(
        "title", "description", "price", "location", "created_at"
    ))
    return JsonResponse({"properties": data})
