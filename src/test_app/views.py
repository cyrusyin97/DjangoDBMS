from django.shortcuts import render
from .models import product
from .models import case
from .models import customer
from .models import purchase
from .models import relate
from .models import support
from .models import Employee
from .models import assign
from .models import salesperson
from .models import sell
from .models import caseComment
from .models import comment
from .models import resolution
from .models import check
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache

from .forms import CaseCreateForm, CustomerCreateForm, RegisterForm, LoginForm, CaseCommentCreateForm, ResolutionCreateForm,\
 CustomerUpdateForm, CaseUpdateForm, SalespersonCreateForm, ProductCreateForm
# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def product_list_view(request):
	product_list = product.objects.all()
	context = {
		"product_list": product_list
	}
	return render(request, "product/product_list_view.html", context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def case_list_view(request):
	case_list = case.objects.all()
	all_caseinfo = []
	for item in case_list:
		c_relate = relate.objects.filter(CaseNo = item.CaseNo)
		c_customer = customer.objects.filter(cid__in = c_relate.values('cid'))

		c_assign = assign.objects.filter(CaseNo = item.CaseNo)
		c_employee = Employee.objects.filter(eid__in = c_assign.values('eid'))

		case_info = {
			"case": case.objects.filter(CaseNo = item.CaseNo),
			"relate_customer": c_customer,
			"assign_employee": c_employee
		}
		all_caseinfo.append(case_info)

	context = {
		"caseinfo": all_caseinfo
	}
	return render(request, "product/case_list_view.html", context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def customer_list_view(request):
	customer_list = customer.objects.all()
	context = {
		"customer_list": customer_list
	}
	return render(request, "product/customer_list_view.html", context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def resolution_list_view(request):
	resolution_list = resolution.objects.all()
	all_info = []
	for item in resolution_list:
		r_check = check.objects.filter(ProductNo = item.ProductNo)
		r_employee = Employee.objects.filter(eid__in = r_check.values('eid'))

		r_product = product.objects.filter(ProductNo = item.ProductNo_id)

		r_info = {
			"resolution": item,
			"product": r_product,
			"employee": r_employee
		}
		all_info.append(r_info)

	context = {
		"resolution_list": all_info
	}
	return render(request, "product/resolution_list_view.html", context)




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def case_detail_view(request):
	if request.GET.get('CaseNo', '') == '':
		return HttpResponseRedirect("/caselist")

	case_detail = case.objects.get(CaseNo = request.GET['CaseNo'])

	c_support = support.objects.filter(CaseNo = request.GET['CaseNo'])
	c_product = product.objects.filter(ProductNo__in = c_support.values('ProductNo'))

	c_relate = relate.objects.filter(CaseNo = request.GET['CaseNo'])
	c_customer = customer.objects.filter(cid__in = c_relate.values('cid'))

	c_assign = assign.objects.filter(CaseNo = request.GET['CaseNo'])
	c_employee = Employee.objects.filter(eid__in = c_assign.values('eid'))

	context = {
		"case": case_detail,
		"product": c_product,
		"customer": c_customer,
		"employee": c_employee
	}
	return render(request, "product/case_detail_view.html", context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def customer_detail_view(request):
	if request.GET.get('cid', '') == '':
		return HttpResponseRedirect("/customerlist")

	customer_detail = customer.objects.get(cid = request.GET['cid'])

	cus_purchase = purchase.objects.filter(cid = request.GET['cid'])
	cus_product = product.objects.filter(ProductNo__in = cus_purchase.values('ProductNo'))

	cus_relate = relate.objects.filter(cid = request.GET['cid'])
	cus_case = case.objects.filter(CaseNo__in = cus_relate.values('CaseNo'))

	context = {
		"customer": customer_detail,
		"product": cus_product,
		"case": cus_case
	}
	print(cus_product)
	print(cus_case)
	return render(request, "product/customer_detail_view.html", context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def salesperson_list_view(request):
	salesperson_list = salesperson.objects.all()
	context = {
		"salesperson_list": salesperson_list
	}
	return render(request, "product/salesperson_list_view.html", context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def salesperson_detail_view(request):
	if request.GET.get('sid', '') == '':
		return HttpResponseRedirect("/salespersonlist")

	salesperson_detail = salesperson.objects.get(sid = request.GET['sid'])

	sp_sell = sell.objects.filter(sid = request.GET['sid'])
	sp_product = product.objects.filter(ProductNo__in = sp_sell.values('ProductNo'))

	context = {
		"salesperson": salesperson_detail,
		"product": sp_product,
	}
	return render(request, "product/salesperson_detail_view.html", context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def casecomment_list_view(request):
	casecomment_list = caseComment.objects.all()
	all_commentinfo = []
	for item in casecomment_list:
		cc_comment = comment.objects.filter(CaseNo = item.CaseNo)
		cc_employee = Employee.objects.filter(eid__in = cc_comment.values('eid'))

		cc_case = case.objects.filter(CaseNo = item.CaseNo_id)

		comment_info = {
			"comment": item,
			"employee": cc_employee,
			"case": cc_case
		}
		all_commentinfo.append(comment_info)

	context = {
		"comment_info": all_commentinfo
	}
	return render(request, "product/casecomment_list_view.html", context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def case_create_view(request):
	form = CaseCreateForm()
	if request.method == "POST":
		form = CaseCreateForm(request.POST)
		if form.is_valid():
			newcase = case.objects.create(
				summary = form.cleaned_data['summary'],
				status = form.cleaned_data['status'],
				cdescription = form.cleaned_data['description'],
				timeframe = form.cleaned_data['timeframe']
			)
			for i in form.cleaned_data['product_support']:
				purchase.objects.create(
					ProductNo_id = i,
					cid_id = form.cleaned_data['customer_relate']
				)

				support.objects.create(
					ProductNo_id = i,
					CaseNo_id = newcase.CaseNo
				)
			newrelate = relate.objects.create(
				cid_id = form.cleaned_data['customer_relate'],
				CaseNo_id = newcase.CaseNo
			)
			newassign = assign.objects.create(
				eid_id = form.cleaned_data['employee_assign'],
				CaseNo_id = newcase.CaseNo
			)

			return HttpResponseRedirect("/caselist")
			print(form.cleaned_data)

	context = {
		"form": form
	}
	return render(request, "product/case_create_view.html", context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def customer_create_view(request):
	form = CustomerCreateForm()
	if request.method == "POST":
		form = CustomerCreateForm(request.POST)
		if form.is_valid():
			if (customer.objects.filter(cname = form.cleaned_data['name']).exists()):
				#messages.success(request, 'Customer Already Exsits!')
				return HttpResponseRedirect("/customerlist")
			newcustomer = customer.objects.create(
				cname = form.cleaned_data['name'],
				caddress = form.cleaned_data['address'],
				cga_income = form.cleaned_data['cga_income'],
				company = form.cleaned_data['company']
			)
			print(form.cleaned_data)
			return HttpResponseRedirect("/customerlist")

	context = {
		"form": form
	}
	return render(request, "product/customer_create_view.html", context)




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def product_create_view(request):
	form = ProductCreateForm()
	if request.method == "POST":
		form = ProductCreateForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			new_product = product.objects.create(
				pname = form.cleaned_data['name'],
				pdescription = form.cleaned_data['description'],
			)
			sell_by_sp = salesperson.objects.get(sid = form.cleaned_data['salesperson'])
			#print(form.cleaned_data)
			new_sell = sell.objects.create(
				sid_id = form.cleaned_data['salesperson'],
				ProductNo_id = new_product.ProductNo
			)
			
			return HttpResponseRedirect("/productlist")

	context = {
		"form": form
	}
	return render(request, "product/product_create_view.html", context)






@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def customer_update_view(request):
	form = CustomerUpdateForm()
	if request.method == "POST":
		form = CustomerUpdateForm(request.POST)
		if form.is_valid():
			update_customer = customer.objects.get(cid = form.cleaned_data['customer_relate'])
			update_customer.cname = form.cleaned_data['name']
			update_customer.caddress = form.cleaned_data['address']
			update_customer.cga_income = form.cleaned_data['cga_income']
			update_customer.company = form.cleaned_data['company']
			print(form.cleaned_data)
			update_customer.save()
			return HttpResponseRedirect("/customerlist")

	context = {
		"form": form
	}
	return render(request, "product/customer_update_view.html", context)




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def case_update_view(request):
	form = CaseUpdateForm()
	if request.method == "POST":
		form = CaseUpdateForm(request.POST)
		if form.is_valid():
			update_case = case.objects.get(CaseNo = form.cleaned_data['old_case'])
			update_case.summary = form.cleaned_data['summary']
			update_case.status = form.cleaned_data['status']
			update_case.description = form.cleaned_data['description']
			update_case.timeframe = form.cleaned_data['timeframe']
			print(form.cleaned_data)
			update_case.save()
			return HttpResponseRedirect("/caselist")

	context = {
		"form": form
	}
	return render(request, "product/case_update_view.html", context)





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def casecomment_create_view(request):
	form = CaseCommentCreateForm()
	if request.method == "POST":
		form = CaseCommentCreateForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			new_casecomment = caseComment.objects.create(
				CaseNo_id = form.cleaned_data['cc_case'],
				time = form.cleaned_data['timeframe'],
				comment = form.cleaned_data['cc_comment'],
			)
			current_employee = Employee.objects.get(ename = request.user.username)
			#print(form.cleaned_data)
			new_comment = comment.objects.create(
				CaseNo_id = form.cleaned_data['cc_case'],
				eid_id = current_employee.eid
			)
			
			return HttpResponseRedirect("/casecommentlist")

	context = {
		"form": form
	}
	return render(request, "product/casecomment_create_view.html", context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def resolution_create_view(request):
	form = ResolutionCreateForm()
	if request.method == "POST":
		form = ResolutionCreateForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			new_resolution = resolution.objects.create(
				ProductNo_id = form.cleaned_data['r_product'],
				cm_resolution = form.cleaned_data['cm_resolution'],
				step = form.cleaned_data['step'],
			)
			current_employee = Employee.objects.get(ename = request.user.username)
			#print(form.cleaned_data)
			new_check = check.objects.create(
				ProductNo_id = form.cleaned_data['r_product'],
				eid_id = current_employee.eid
			)
			
			return HttpResponseRedirect("/resolutionlist")

	context = {
		"form": form
	}
	return render(request, "product/resolution_create_view.html", context)




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def salesperson_create_view(request):
	form = SalespersonCreateForm()
	if request.method == "POST":
		form = SalespersonCreateForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			new_salesperson = salesperson.objects.create(
				sname = form.cleaned_data['name'],
				semail = form.cleaned_data['email'],
				job_title = form.cleaned_data['job_title'],
			)
			for item in form.cleaned_data['product_sell']:
				new_sell = sell.objects.create(
					ProductNo_id = item,
					sid_id = new_salesperson.sid
				)
			
			return HttpResponseRedirect("/salespersonlist")

	context = {
		"form": form
	}
	return render(request, "product/salesperson_create_view.html", context)





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def customer_query_view(request):
	allcustomer = customer.objects.all()
	query_result = allcustomer
	flag = False
	if request.GET.get('name', '') : 
		query_result = query_result.filter(cname = request.GET['name'])
		flag = True

	if request.GET.get('company', ''):
		query_result = query_result.filter(company = request.GET['company'])
		flag = True
		
	if request.GET.get('income', ''):
		if request.GET['income'] == 'ascending':
			query_result = query_result.order_by('cga_income')
		if request.GET['income'] == 'descending':
			query_result = query_result.order_by('-cga_income')
		flag = True

	context = {
		"result": query_result
	}
	if flag == True:
		return render(request, "product/customer_query_view.html", context)
	else :
		return HttpResponseRedirect("/customerlist")




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def resolution_query_view(request):
	if request.GET.get('product', '') : 
		res_product = product.objects.filter(pname = request.GET['product'])
		r_result = resolution.objects.filter(ProductNo__in = res_product.values('ProductNo'))
		print(r_result)

		context = {
			"r_product": res_product,
			"resolution_list": r_result
		}
		return render(request, "product/resolution_query_view.html", context)
	else :
		return HttpResponseRedirect("/resolutionlist")



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def case_aggregation_view(request):
	context = {}
	if request.GET.get('by', '') :
		cus_info = []
		com_info = []
		prod_info = []
		emp_info = []
		info = []
		if request.GET['by'] == "customer":
			for cus in customer.objects.all():
				c_case_count = relate.objects.filter(cid = cus.cid).count()
				if c_case_count > 0:
					cus_info.append((cus.cid, cus.cname, c_case_count))

			cus_info = sorted(cus_info, key=lambda x: x[2], reverse = True)
			t_info = [x[0] for x in cus_info]
			for i in t_info:
				cust = customer.objects.filter(cid = i)
				cust_relate = relate.objects.filter(cid = i)
				cust_case = case.objects.filter(CaseNo__in = cust_relate.values('CaseNo'))

				for k in cust_case:
					c_assign = assign.objects.filter(CaseNo = k.CaseNo)
					c_employee = Employee.objects.filter(eid__in = c_assign.values('eid'))

					cus_info = {
						"relate_customer": cust,
						"case": k,
						"assign_employee": c_employee
					}
					info.append(cus_info)

			context = {
				"caseinfo": info
			}
			print(info)
			return render(request, "product/case_query_view.html", context)
			#return render(request, "product/case_aggregation_view.html", context)

		elif request.GET['by'] == "company":
			company_list = []
			for i in customer.objects.all():
				if i.company not in company_list:
					company_list.append(i.company)

			for company in company_list:
				c_customer = customer.objects.filter(company = company)
				c_case_count = 0
				for i in c_customer:
					c_case_count = c_case_count + relate.objects.filter(cid = i.cid).count()
				if c_case_count > 0:
					com_info.append((company, c_case_count))


			com_info = sorted(com_info, key=lambda x: x[1], reverse = True)

			t_info = [x[0] for x in com_info]

			for i in t_info:
				c_customer = customer.objects.filter(company = i)
				print(c_customer)
				for c in c_customer:
					c_relate = relate.objects.filter(cid = c.cid)
					c_case = case.objects.filter(CaseNo__in = c_relate.values('CaseNo'))

					for k in c_case:
						c_assign = assign.objects.filter(CaseNo = k.CaseNo)
						c_employee = Employee.objects.filter(eid__in = c_assign.values('eid'))

						cus_info = {
							"relate_customer": customer.objects.filter(cid = c.cid),
							"case": k,
							"assign_employee": c_employee
						}
						info.append(cus_info)

			context = {
				"caseinfo": info
			}
			return render(request, "product/case_query_view.html", context)
			#return render(request, "product/case_aggregation_view.html", context)
		
		elif request.GET['by'] == "product":
			for prod in product.objects.all():
				p_case_count = support.objects.filter(ProductNo = prod.ProductNo).count()
				if p_case_count > 0:
					prod_info.append((prod.ProductNo, p_case_count))

			prod_info = sorted(prod_info, key=lambda x: x[1], reverse = True)
			t_info = [x[0] for x in prod_info]
			for i in t_info:
				prod = product.objects.get(ProductNo = i)
				prod_support = support.objects.filter(ProductNo = i)
				prod_case = case.objects.filter(CaseNo__in = prod_support.values('CaseNo'))
				prod_info = {
					"prod": prod,
					"prod_case": prod_case
				}
				info.append(prod_info)

			context = {
				"info": info
			}
			print(info)
			return render(request, "product/case_aggregation_view.html", context)


		elif request.GET['by'] == "employee":
			for emp in Employee.objects.all():
				e_case_count = assign.objects.filter(eid = emp.eid).count()
				if e_case_count > 0:
					emp_info.append((emp.eid, e_case_count))

			emp_info = sorted(emp_info, key=lambda x: x[1], reverse = True)

			t_info = [x[0] for x in emp_info]
			for i in t_info:
				emp = Employee.objects.filter(eid = i)
				emp_assign = assign.objects.filter(eid = i)
				emp_case = case.objects.filter(CaseNo__in = emp_assign.values('CaseNo'))

				for k in emp_case:
					c_relate = relate.objects.filter(CaseNo = k.CaseNo)
					c_customer = customer.objects.filter(cid__in = c_relate.values('cid'))

					cus_info = {
						"relate_customer": c_customer,
						"case": k,
						"assign_employee": emp
					}
					info.append(cus_info)

			context = {
				"caseinfo": info
			}
			print(info)
			return render(request, "product/case_query_view.html", context)
			#return render(request, "product/case_aggregation_view.html", context)



		else:
			return HttpResponseRedirect("/caselist")




		return render(request, "product/case_aggregation_view.html", context)
	

	else :
		return HttpResponseRedirect("/caselist")























@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def case_query_view(request):
	query_result = case.objects.all()
	result = query_result
	flag = False
	if request.GET.get('time', ''):
		if request.GET['time'] == '0':
			result = result.order_by('-timeframe__year', '-timeframe__month', '-timeframe__day')
		if request.GET['time'] == '1':
			result = result.order_by('timeframe__year', 'timeframe__month', 'timeframe__day')
		flag = True
	if request.GET.get('timeframe', ''):
		result = result.filter(timeframe = request.GET['timeframe'])
		flag = True
	if request.GET.get('status', ''):
		result = result.filter(status = request.GET['status'])
		flag = True
	if request.GET.get('customer', ''):
		c_customer = customer.objects.filter(cname = request.GET['customer'])
		c_relate = relate.objects.filter(cid__in = c_customer.values('cid'))
		result = result.filter(CaseNo__in = c_relate.values('CaseNo'))
		flag = True
	if request.GET.get('company', ''):
		c_customer = customer.objects.filter(company = request.GET['company'])
		c_relate = relate.objects.filter(cid__in = c_customer.values('cid'))
		result = result.filter(CaseNo__in = c_relate.values('CaseNo'))
		flag = True
	if request.GET.get('product', ''):
		c_product = product.objects.filter(pname = request.GET['product'])
		c_support = support.objects.filter(ProductNo__in = c_product.values('ProductNo'))
		result = result.filter(CaseNo__in = c_support.values('CaseNo'))
		flag = True
	if request.GET.get('employee', ''):
		c_employee = Employee.objects.filter(ename = request.GET['employee'])
		c_assign = assign.objects.filter(eid__in = c_employee.values('eid'))
		result = result.filter(CaseNo__in = c_assign.values('CaseNo'))
		flag = True

	all_caseinfo = []
	for item in result:
		c_relate = relate.objects.filter(CaseNo = item.CaseNo)
		c_customer = customer.objects.filter(cid__in = c_relate.values('cid'))

		c_assign = assign.objects.filter(CaseNo = item.CaseNo)
		c_employee = Employee.objects.filter(eid__in = c_assign.values('eid'))

		case_info = {
			"case": item,
			"relate_customer": c_customer,
			"assign_employee": c_employee
		}
		all_caseinfo.append(case_info)

	context = {
		"caseinfo": all_caseinfo
	}

	if flag == True:
		return render(request, "product/case_query_view.html", context)
	else:
		return HttpResponseRedirect("/caselist")

	

















@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def home_view(request):
	return render(request, "product/home_view.html")


def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			if (User.objects.filter(username = form.cleaned_data['username']).exists()):
				messages.info(request, 'Username Already Exsits!')
				return HttpResponseRedirect("/login")

			if (Employee.objects.filter(eemail = form.cleaned_data['email']).exists()):
				messages.info(request, 'Email Already Registered')
				return HttpResponseRedirect("/login")

			new_user = User.objects.create_user(
				form.cleaned_data['username'],
				form.cleaned_data['email'],
				form.cleaned_data['password']
			)
			new_employee = Employee.objects.create(
				ename = form.cleaned_data['username'],
				eaddress = form.cleaned_data['address'],
				phone = form.cleaned_data['phone'],
				eemail = form.cleaned_data['email']
			)
			print(form.cleaned_data)
			return HttpResponseRedirect("/login")
	context = {
		"form": form
	}
	return render(request, "auth/register_view.html", context)


@never_cache
def login_view(request):
	if not request.user.is_authenticated:
		form = LoginForm()
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
				print(form.cleaned_data)
				if user is not None:
					login(request, user)
					user_info = {
						"user_info": request.user
					}
					return HttpResponseRedirect("/home")
				else :
					err_info = {
						"form": form,
						"err_msg": "Please enter the correct username and password."
					}
					messages.info(request, 'Please enter the correct username and password.')
					return HttpResponseRedirect("/login")
		context = {
			"form": form
		}
		return render(request, "auth/login_view.html", context)
	else:
		return HttpResponseRedirect("/home")


def logout_view(request):
    logout(request)
    messages.info(request, 'You are Logged Out!')
    return HttpResponseRedirect("/login")












