from django.shortcuts import (
    render, render_to_response, 
    get_object_or_404, get_list_or_404, 
    redirect, HttpResponse
)
from django.views.generic import View, ListView


from SpiderBT_Cases.models import Product


class IndexTaskView(View):
    template_name = ''

    def get(self, request, slug):
        product = Product.objects.filter(slug=slug)

        if product:
            return HttpResponse('view tasks for the product')
        
        return HttpResponse('no product')

class CreateTaskView(View):

    def get(self, request, slug):
        product = Product.objects.filter(slug=slug)
        
        if product:
            return HttpResponse('create task for the product')
        
        return HttpResponse('create task')
