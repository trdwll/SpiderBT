from django.conf import settings

from SpiderBT_Cases.models import Product

def global_settings(request):
    return {
        'PRODUCTS': Product.objects.all()
    }