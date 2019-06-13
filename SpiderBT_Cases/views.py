from django.shortcuts import (
    render, redirect,
    get_object_or_404, get_list_or_404, 
    HttpResponse
)
from django.views.generic import View
from django.contrib.auth.models import User
from django.db.models import Q

from SpiderBT_Cases.models import Product, Case, CaseNote, CaseVote


class AllCasesView(View):
    template_name = 'cases/view-all.html'

    def get(self, request):
        return HttpResponse('view for all cases')


class CasesView(View):
    template_name = 'cases/view-all-product.html'

    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)

        opened_cases = Case.objects.filter(product=product, status='open', visibility='public').order_by('-id')[:30]
        closed_cases = Case.objects.filter(Q(status='closed') | Q(status='fixed'), visibility='public', product=product).order_by('-id')[:30]

        return render(request, self.template_name, {'product': product, 'opened_cases': opened_cases, 'closed_cases': closed_cases})
        

class CaseView(View):
    template_name = 'cases/case/view-case.html'

    def get(self, request, case_id):
        case = get_object_or_404(Case, identifier=case_id)

        case_notes = CaseNote.objects.filter(case=case)
        votes = CaseVote.objects.filter(case=case).count()

        has_voted = request.user.is_authenticated and CaseVote.objects.filter(author=User.objects.get(username=request.user.username), case=case).exists()

        return render(request, self.template_name, {'case': case, 'case_notes': case_notes, 'votes': votes, 'has_voted': has_voted})


class CaseVoteView(View):   
    def get(self, request, case_id):
        return redirect('view_case_page', case_id=case_id)

    def post(self, request, case_id):
        if not request.user.is_authenticated:
            return redirect('view_case_page', case_id=case_id)

        case = get_object_or_404(Case, identifier=case_id)

        requested_user = User.objects.get(username=request.user.username)
        has_voted = CaseVote.objects.filter(case=case, author=requested_user).exists()

        if not has_voted:
            CaseVote.objects.create(author=requested_user, case=case)
        
        return redirect('view_case_page', case_id=case_id)



class SubmitCaseView(View):
    template_name = 'cases/submit-case.html'

    def get(self, request):
        return HttpResponse('submit a case')

    def post(self, request):
        pass