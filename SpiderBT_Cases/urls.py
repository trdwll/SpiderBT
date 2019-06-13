from django.urls import path

from SpiderBT_Cases.views import (
    AllCasesView, 
    CasesView, CaseView, 
    CaseVoteView, 
    SubmitCaseView
)

urlpatterns = [
    path('<slug>/cases/', CasesView.as_view(), name='view_cases'),
    path('case/<case_id>/', CaseView.as_view(), name='view_case_page'),
    path('case/<case_id>/vote/', CaseVoteView.as_view(), name='vote_case'),
    path('submit-case/', SubmitCaseView.as_view(), name='submit_case'),
]
