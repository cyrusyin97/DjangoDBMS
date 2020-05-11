"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from test_app.views import product_list_view, case_list_view, case_detail_view, customer_detail_view,\
case_create_view, home_view, customer_list_view, customer_create_view, register_view, login_view, logout_view,\
customer_query_view, salesperson_list_view, salesperson_detail_view, casecomment_list_view, casecomment_create_view,\
case_query_view, resolution_list_view, resolution_create_view, customer_update_view, case_update_view, resolution_query_view,\
salesperson_create_view, case_aggregation_view, product_create_view

urlpatterns = [
	path('', login_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('home/', home_view),
    path('admin/', admin.site.urls),
    path('productlist/', product_list_view),
    path('caselist/', case_list_view),
    path('casedetail/', case_detail_view),
    path('customerdetail/', customer_detail_view),
    path('casecreate/', case_create_view),
    path('customerlist/', customer_list_view),
    path('customercreate/', customer_create_view),
    path('customerquery/', customer_query_view),
    path('salespersonlist/', salesperson_list_view),
    path('salespersondetail/', salesperson_detail_view),
    path('casecommentlist/', casecomment_list_view),
    path('casecommentcreate/', casecomment_create_view),
    path('casequery/', case_query_view),
    path('resolutionlist/', resolution_list_view),
    path('resolutioncreate/', resolution_create_view),
    path('customerupdate/', customer_update_view),
    path('caseupdate/', case_update_view),
    path('resolutionquery/', resolution_query_view),
    path('salespersoncreate/', salesperson_create_view),
    path('caseaggregation/', case_aggregation_view),
    path('productcreate/', product_create_view),
]
