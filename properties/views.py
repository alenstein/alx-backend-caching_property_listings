from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15) # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    data = serialize("json", properties)
    return JsonResponse(data, content_type="application/json")
