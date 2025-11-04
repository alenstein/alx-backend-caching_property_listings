from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15) # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    data = serialize("json", properties)
    return HttpResponse(data, content_type="application/json")
