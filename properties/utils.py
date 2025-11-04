import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

# Configure logging
logger = logging.getLogger(__name__)

def get_all_properties():
    """ 
    Retrieves all properties, using the cache if available.
    """
    queryset = cache.get('all_properties')
    if queryset is None:
        logger.info("Cache miss for 'all_properties'. Fetching from database.")
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)  # Cache for 1 hour
    else:
        logger.info("Cache hit for 'all_properties'. Serving from cache.")
    return queryset

def get_redis_cache_metrics():
    """
    Retrieves and analyzes Redis cache hit/miss metrics.
    """
    try:
        conn = get_redis_connection("default")
        info = conn.info()
        
        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)
        total_lookups = hits + misses
        
        hit_ratio = (hits / total_lookups) * 100 if total_lookups > 0 else 0
        
        metrics = {
            'hits': hits,
            'misses': misses,
            'hit_ratio': f'{hit_ratio:.2f}%'
        }
        
        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics
    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {'error': str(e)}
