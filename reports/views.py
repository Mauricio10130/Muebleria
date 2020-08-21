from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from reports.forms import ReportForm

class ReportSaleView(TemplateView):
	template_name = 'sale/report.html' 
	
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Reporte de las Ventas'
		context['form'] = ReportForm()
		return context   