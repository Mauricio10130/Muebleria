from django.urls import path

from . import views
from reports.views import ReportSaleView

app_name = 'reports'

urlpatterns = [
	path('sale/', views.ReportSaleView.as_view(), name='sale_report'),
]       