from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Goods
from django.views.generic import CreateView, ListView

from django.contrib.auth.decorators import login_required


def Proba(request):
    last_ten = Goods.objects.order_by('-id')[:10]
    return render(request, 'gui/home.html', context={"goods": last_ten})


class GoodCreateView(CreateView):
    model = Goods
    fields = ['name', 'quantity', "price"]
    success_url = 'http://127.0.0.1:8000/'
    # template_name = "revision_app/base.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GoodCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['goods'] = Goods.objects.order_by('-id')[:5]
        return context

def about(request):
    return render(request, template_name="gui/about.html")