from django.shortcuts import render
from django.views.generic.list import ListView
from facture.models import Facture
from django.views.generic.detail import DetailView

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG



# Create your views here.

class FactureListView(ListView):
    model = Facture

class FactureDetailView(DetailView):
    model = Facture

class FacturePDFView(WeasyTemplateResponseMixin, FactureDetailView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    # pdf_stylesheets = [
    #     settings.STATIC_ROOT + 'css/app.css',
    # ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # suggested filename (is required for attachment!)
    pdf_filename = 'foo.pdf'
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, ** kwargs)

        context['pdf']= True
        return context
        