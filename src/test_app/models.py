from django.db import models
from django.utils.timezone import now
# Create your models here.
class product(models.Model):
	ProductNo	= models.AutoField(primary_key = True)
	pname 		= models.CharField(max_length = 32, unique = True)
	pdescription = models.TextField(blank = True, null = True, max_length = 255)
	#CaseNo		= models.ForeignKey('case', on_delete = models.CASCADE)
	#CID			= models.ForeignKey('customer', on_delete = models.CASCADE)
	#SID			= models.ForeignKey('salesperson', on_delete = models.CASCADE)


class customer(models.Model):
	cid			= models.AutoField(primary_key = True, db_index = True)
	cname 		= models.CharField(max_length = 32)
	caddress	= models.CharField(max_length = 32)
	cga_income	= models.DecimalField(max_digits=32, decimal_places=2)
	company		= models.CharField(max_length = 32, default = "")
	#ProductNo	= models.ForeignKey('Product', on_dzelete = models.CASCADE)
	#CaseNo		= models.ForeignKey('case', on_delete = models.CASCADE)


class case(models.Model):
	CaseNo		= models.AutoField(primary_key = True, db_index = True)
	summary		= models.TextField(blank = True, null = True, max_length = 255)
	status		= models.BooleanField(default = False)
	cdescription = models.TextField(blank = True, null = True, max_length = 255)
	timeframe	= models.DateField(default = now)
	#CID			= models.ForeignKey('customer', on_delete = models.CASCADE)
	#EID			= models.ForeignKey('Employee', on_delete = models.CASCADE)
	#ProductNo	= models.ForeignKey('Product', on_delete = models.CASCADE)


class salesperson(models.Model):
	sid			= models.AutoField(primary_key = True)
	sname		= models.CharField(max_length = 32)
	semail		= models.EmailField()
	job_title	= models.CharField(max_length = 16)
	#ProductNo	= models.ForeignKey('Product', on_delete = models.CASCADE)


class Employee(models.Model):
	eid			= models.AutoField(primary_key = True)
	ename		= models.CharField(max_length = 32, unique = True)
	eaddress		= models.CharField(max_length = 32)
	phone		= models.CharField(max_length = 32)
	eemail		= models.EmailField(unique = True)
	#CaseNo		= models.ForeignKey('case', on_delete = models.CASCADE)
	#ProductNo	= models.ForeignKey('Product', on_delete = models.CASCADE)


class resolution(models.Model):
	ProductNo	= models.ForeignKey('product', on_delete = models.CASCADE)
	cm_resolution = models.TextField(blank = True, null = True, max_length = 255)
	step		= models.TextField(blank = True, null = True, max_length = 255)
	


class caseComment(models.Model):
	CaseNo      = models.ForeignKey('case', on_delete = models.CASCADE)
	time		= models.DateField()
	comment 	= models.TextField(blank = True, null = True, max_length = 255)
	#eid			= models.ForeignKey('Employee', on_delete = models.CASCADE)


class purchase(models.Model):
	ProductNo	= models.ForeignKey('product', on_delete = models.CASCADE)
	cid			= models.ForeignKey('customer', on_delete = models.CASCADE)


class relate(models.Model):
	cid			= models.ForeignKey('customer', on_delete = models.CASCADE)
	CaseNo		= models.ForeignKey('case', on_delete = models.CASCADE)


class support(models.Model):
	ProductNo	= models.ForeignKey('product', on_delete = models.CASCADE)
	CaseNo		= models.ForeignKey('case', on_delete = models.CASCADE)


class assign(models.Model):
	CaseNo		= models.ForeignKey('case', on_delete = models.CASCADE)
	eid			= models.ForeignKey('Employee', on_delete = models.CASCADE)


class comment(models.Model):
	eid			= models.ForeignKey('Employee', on_delete = models.CASCADE)
	CaseNo		= models.ForeignKey('case', on_delete = models.CASCADE)


class sell(models.Model):
	ProductNo	= models.ForeignKey('product', on_delete = models.CASCADE)
	sid			= models.ForeignKey('salesperson', on_delete = models.CASCADE)


class apply(models.Model):
	ProductNo	= models.ForeignKey('product', on_delete = models.CASCADE)


class check(models.Model):
	ProductNo	= models.ForeignKey('product', on_delete = models.CASCADE)
	eid			= models.ForeignKey('Employee', on_delete = models.CASCADE)


















