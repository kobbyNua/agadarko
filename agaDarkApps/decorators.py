from django.http import HttpResponse
from django.shortcuts import redirect
from . import models

'''
login decorators
redirecting staff to pages if password is still default

'''

def unauthenicated_user(view_func):
	def func_wrapper(reequest,*args,**kwargs):
		if not request.user.is_authenticated:
			return request('./login')
		else:
			view_func(request,*args,**kwargs)
	return  func_wrapper
'''
users will be logged out if he.she doesn't belong to any hospital
admins' will be forced to create hospital details if hospital details are not found
'''
def hospital_ddetails_set_up(view_func):
	def func_wrapper(request,*args,**kwargs):
		if request.user.is_superuser == True:
			view_hospitals=Hospital.objects.filter(adminstrator=request.user.id)
			if not view_hospitals.exist():
				return redirect('./set-up-hospital')
		else:
			hospital_staffs=Hospital_Staff.objects.filter(staff=request.user.id)
			if not hospital_staffs.exist():
				return request('./login')
	return func_wrapper

'''
   groups to be defiend includes admin,nurses,doctors,lab technician,dietary and accountants
'''

def allowed_user(allowed_roles=[]):
	def decorator(view_func):
		def func_wrapper(request,*args,**kwargs):
			group=None
			if request.user.group.exist():
				group=request.user.groups.all()[0].name
			if group in allowed_roles:
				view_func(request,*args,**kwargs)
			else:
				redirect('./dashboard')
		return func_wrapper
	return decorator

