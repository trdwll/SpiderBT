from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib.auth.views import LogoutView

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home_page'),

    path('', include('SpiderBT_Cases.urls')),
    path('', include('SpiderBT_Scrum.urls')),


    # Static pages
    # TODO: Add ToS/PP templates
    

    # Social Auth urls
    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/logout/', LogoutView.as_view(next_page='/'), name='auth_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)