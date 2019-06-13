from django.shortcuts import (
    render,
    redirect, HttpResponse
)
from django.views.generic import View
from django.db.models import Q

from SpiderBT_Cases.models import (
    Case
)



class HomeView(View):
    template_name = 'home_page.html'

    def get(self, request):
        opened_cases = Case.objects.filter(status='open', visibility='public').order_by('-id')[:15]
        closed_cases = Case.objects.filter(Q(status='closed') | Q(status='fixed'), visibility='public').order_by('-id')[:15]

        return render(request, self.template_name, {'opened_cases': opened_cases, 'closed_cases': closed_cases})