from django.core.cache import cache
from .models import Property

def get_all_properties():
    """ 
    Retrieves all properties, using the cache if available.
    """
    queryset = cache.get('all_properties')
    if queryset is None:
        queryset = Property.objects.all()
        # Cache for 1 hour (3600 seconds)
        cache.set('all_properties', queryset, 3600)
    return queryset
