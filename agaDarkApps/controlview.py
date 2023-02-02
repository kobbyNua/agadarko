from django.contrib.auth.models import User,auth,Group
from .models import Region,Hospital,Hospital_Staff
from django.db.models import Count ,F,Q,Sum
from datetime import datetime

'''
    stage 1
'''
def  create_hospital_details(name,user,email,telephone,town,regions):

		get_hospital_name=Hospital.objects.filter(name=name)
		if not get_hospital_name.exists():
			create_hospital=Hospital.objects.create(name=name,adminstrator=User.objects.get(pk=user),telephone=telephone,email=email,Town=town,region=Region.objects.get(pk=regions))
			create_hospital.save()
			return True
		else:

			return False

def getHospital_details(user_id):
       return Hospital.objects.get(adminstrator=user_id)


def view_group():
	    return Group.objects.all()
def create_groups(group_name):
	for groups in range(len(group_name)):
		group=Group.objects.create(name=groups[group_name])
		group.save()
def edit_groups(new_group_name,group_id):
           group=Group.objects.get(pk=group_id)
           group.name=new_group_name
           group.save()
'''
def view_permission():
	      return Permissions.objects.all()

def add_permission(permission,context):
	   for items in range(len(permission)):
	       permissions=Permissions.objects.create(name=permission[items],context=context[items])
	       permissions.save()
def edit_permission(new_permission,permission_id,context):
           permission=Permissions.objects.get(pk=permission_id)
           permission.name=new_permission
           permission.context=context
           permission.save()
def view_group_permissions():
	       return Group_Persmission.objects.all()
def add_group_permissions(group_id,permission_id):
           create_group_permission=Group_Persmission.create.objects(group=Group.objects.get(pk=group_id),permission=Permissions.objects.get(pk=permission_id))
           create_group_permission.save()
def edit_group_permissions(group_id,permission_id,group_permission_id):
            group_permission=Group_Persmission.objects.get(pk=group_permission_id)
            group_permission.group.id=group_id
            group_permission.permission.id=group_permission_id
'''

def create_staff(first_name,last_name,email,username,telephone,group_id,user_id):
	check_user=User.objects.filter(Q(email=email)|Q(username=username))
	if not check_user.exists():
		default_password='Password@1'
		hospital_info=get_user_hospital_details(user_id)
		#hospital_info=Hospital.objects.filter(adminstrator__id=user_id)
		hospital_id=""
		users=User.objects.create_user(username=username,password=default_password,first_name=first_name,last_name=last_name,email=email)
		users.save()
		user_id=User.objects.latest('id')
		'''
		for hospitals in hospital_info:
			hospital_id+=str(hospitals.id)
		print(hospital_id)
		'''
		hospital_staffs(user_id.id,telephone,hospital_info["hospital_id"])
		for groups in range(len(group_id)):
			get_group=Group.objects.get(pk=group_id[groups])
			get_group.user_set.add(user_id.id)
		return True
	else:
		return False




def view_all_staffs():
	admin_id=1
	return Hospital_Staff.objects.filter(hospital__adminstrator=admin_id)
def staff_detail(email):
	staff=User.objects.get(email=email)
	return staff 
def  hospital_staffs(user_id,telephone,hospital_id):

	create_hospital_staff=Hospital_Staff.objects.create(staff=User.objects.get(pk=user_id),telephone=telephone,hospital=Hospital.objects.get(pk=hospital_id))
	create_hospital_staff.save()

	#create_hospital_staff=Hospital_Staff.objects.create(staff=User.objects.get(pk=user_id),telephone=telephone,hospital=Hospital.objects.get(pk=hospital_id))
	#create_hospital_staff.save()   
def edit_staff(email,first_name,last_name,username,telephone,user_id,hostpital_staff_id):
    get_staff=User.objects.get(pk=user_id)
    get_staff.first_name=first_name
    get_staff.last_name=last_name
    get_staff.username=username
    get_staff.save()

    get_hospital_staff_id = Hospital_Staff.objects.get(pk=hostpital_staff_id)
    get_hospital_staff_id.telephone = telephone
    get_hospital_staff_id.save()
    return True
def change_staff_password(password,new_password,user_id):
	if password == new_password:
		staff_detail=User.objects.get(pk=user_id)
		staff_detail.set_password(new_password)
		staff_detail.save()
		return True
	else:
	    return False
def reset_password(user_id):
	user=User.objects.get(pk=user_id)
	user.set_password('Password@1')
	return True
def  region(region_name):
	create_region=Region.objects.create(region=region_name)
	create_region.save()

def get_user_details(user_id):
	return User.objects.get(pk=user_id)

def get_user_hospital_details(user_id):
	get_user=User.objects.get(pk=user_id)
	details={}
	if get_user.is_superuser:
		get_hospital_details=Hospital.objects.get(adminstrator__id=user_id)
		details.update({'user_id':user_id,"hospital_id":get_hospital_details.id})
	else:
		get_hospital_details=Hospital_Staff.objects.get(staff__id=user_id)
		details.update({'user_id':user_id,'hospital_id':get_hospital_details.hospital.id})
	return details


