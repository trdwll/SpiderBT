from django.conf import settings


def global_settings(request):
    return {
        'ENABLE_REGISTRATION': settings.ENABLE_REGISTRATION,
        'ENABLE_OAUTH': settings.ENABLE_OAUTH,
        'ENABLE_LOCAL_AUTH': settings.ENABLE_LOCAL_AUTH
    }