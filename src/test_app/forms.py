from django import forms
from .models import product
from .models import case
from .models import customer
from .models import purchase
from .models import relate
from .models import support
from .models import Employee
from .models import salesperson


class CaseCreateForm(forms.Form):
	summary		= forms.CharField()
	status		= forms.BooleanField(required = False)
	description = forms.CharField(widget=forms.Textarea)
	timeframe	= forms.DateField()
	product_support = forms.MultipleChoiceField()
	customer_relate = forms.ChoiceField()
	employee_assign = forms.ChoiceField()
	def __init__(self, *args, **kwargs):
		super(CaseCreateForm, self).__init__(*args, **kwargs)
		self.fields['product_support'].widget = forms.CheckboxSelectMultiple()
		self.fields['product_support'].choices = product.objects.all().values_list('ProductNo', 'pname')
		self.fields['customer_relate'].choices = customer.objects.all().values_list('cid', 'cname')
		self.fields['employee_assign'].choices = Employee.objects.all().values_list('eid', 'ename')



class CaseUpdateForm(forms.Form):
	old_case = forms.ChoiceField()
	summary		= forms.CharField()
	status		= forms.BooleanField(required = False)
	description = forms.CharField(widget=forms.Textarea)
	timeframe	= forms.DateField()
	def __init__(self, *args, **kwargs):
		super(CaseUpdateForm, self).__init__(*args, **kwargs)
		self.fields['old_case'].choices = case.objects.all().values_list('CaseNo', 'summary')


	

class CustomerCreateForm(forms.Form):
	name		= forms.CharField()
	address		= forms.CharField()
	cga_income	= forms.DecimalField()
	company		= forms.CharField()



class ProductCreateForm(forms.Form):
	name		= forms.CharField()
	description = forms.CharField(widget=forms.Textarea)
	salesperson = forms.ChoiceField()
	def __init__(self, *args, **kwargs):
		super(ProductCreateForm, self).__init__(*args, **kwargs)
		self.fields['salesperson'].choices = salesperson.objects.all().values_list('sid', 'sname')




class CustomerUpdateForm(forms.Form):
	customer_relate = forms.ChoiceField()
	name		= forms.CharField()
	address		= forms.CharField()
	cga_income	= forms.DecimalField()
	company		= forms.CharField()
	def __init__(self, *args, **kwargs):
		super(CustomerUpdateForm, self).__init__(*args, **kwargs)
		self.fields['customer_relate'].choices = customer.objects.all().values_list('cid', 'cname')



class CaseCommentCreateForm(forms.Form):
	timeframe = forms.DateField()
	cc_case = forms.ChoiceField()
	cc_comment = forms.CharField(widget=forms.Textarea)
	def __init__(self, *args, **kwargs):
		super(CaseCommentCreateForm, self).__init__(*args, **kwargs)
		self.fields['cc_case'].choices = case.objects.all().values_list('CaseNo', 'summary')


resolution_choice = (
        ('Refund', 'Refund'),
        ('Return', 'Return'),
        ('Exchange', 'Exchange'),)

class ResolutionCreateForm(forms.Form):
	r_product = forms.ChoiceField()
	cm_resolution = forms.ChoiceField(choices = resolution_choice)
	step = forms.CharField(widget=forms.Textarea(attrs={'class' : 'text_field'}))
	def __init__(self, *args, **kwargs):
		super(ResolutionCreateForm, self).__init__(*args, **kwargs)
		self.fields['r_product'].choices = product.objects.all().values_list('ProductNo', 'pname')




class SalespersonCreateForm(forms.Form):
	name		= forms.CharField(widget = forms.TextInput(attrs={'class' : 'text_field'}))
	email		= forms.EmailField(widget = forms.EmailInput(attrs={'class' : 'text_field'}))
	job_title	= forms.CharField(widget = forms.TextInput(attrs={'class' : 'text_field'}))
	product_sell = forms.MultipleChoiceField()
	def __init__(self, *args, **kwargs):
		super(SalespersonCreateForm, self).__init__(*args, **kwargs)
		self.fields['product_sell'].widget = forms.CheckboxSelectMultiple()
		self.fields['product_sell'].choices = product.objects.all().values_list('ProductNo', 'pname')




class RegisterForm(forms.Form):
	username	= forms.CharField(widget = forms.TextInput(attrs={'class' : 'text_field'}))
	password	= forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'text_field'}))
	email		= forms.EmailField(widget = forms.EmailInput(attrs={'class' : 'text_field'}))
	address		= forms.CharField(widget = forms.TextInput(attrs={'class' : 'text_field'}))
	phone		= forms.CharField(widget = forms.TextInput(attrs={'class' : 'text_field'}))


class LoginForm(forms.Form):
	username	= forms.CharField(widget = forms.TextInput(attrs={'class' : 'text_field'}))
	password	= forms.CharField(widget = forms.PasswordInput(attrs={'class' : 'text_field'}))










