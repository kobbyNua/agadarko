from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,FileResponse
from django.contrib.auth.models import User,auth,Group
from .models import Hospital_Staff,Patient_Diagosis_History
from .patients import patient_search,patient_history_details,patient_medical_diagnosis_records,Check_in_patient_search,patient_check_in_list,paitient_opd_visiting_history,getRegion,view_patient_details,patient,create_opd_vitals,edit_opd_vitals,opd_vitals,patinet_waiting_list,view_paitent_opd_reports,doctor_diagonsis,send_lab_request,send_dietary_request,patient_opd_history_vitals,view_patient_diagnosis_complaints,doctor_diagonsis,patient_diagonsis_history,send_lab_request,view_patient_lab_test_report,patient_lab_report_result,view_patient_lab_report_status,getPatientDiagnosisId,patient_dietary_status
from .laboratory import view_lab_test_list,patient_laboratory_records_history,lab_patient_search,multiple_lab_type_list,getLaboratory,edit_lab_test_list_details,view_patient_lab_details,patient_laboratory,create_lab_test_details_cost,input_patient_lab_request,view_lab_test_request,view_lab_test_request,view_patint_lab_history,view_patient_lab_details
from .dietary import view_patient_deietary_details,multiple_dietary_list,dietary_need_restock,update_dietary_details,deitary_stock_info,update_dietary_details_stock,view_dietary_list,create_dietary_supplementary_cost,view_patient_deietary_details,view_dietary_pending_list,input_patient_dietry_request,dietary_supplement_stocking,dietary_supplement_stocking_details_history
from .controlview import create_hospital_details,view_all_staffs,create_staff,edit_staff,change_staff_password
#from .controlview import hospital,view_all_staffs,staff_detail,create_groups,edit_groups,getHospital_details,patient_details,patient,opd_vitals,create_opd_vitals,edit_opd_vitals,patient_opd_history_vitals
#from .decorators import unauthenicated_user,hospital_ddetails_set_up
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BooksSerializers,RegionSerializers
'''
import json
from .models import Books,Region




def dashboard(request):
	return render(request,'dashboard/dashboard.html',{'title':'dashboard','page_title':'Dashboard','path':'home'})


def patient_opd_panel(request):
	'''
       present the nurse with a view to either search for a patient or register a patient
	'''
	regions=getRegion()
	in_patient_list=patient_check_in_list()
	return render(request,'dashboard/patients/opd-patient-records.html',{'title':'Patient OPD Records'.upper(),'page_title':'Patient Records','in_patient_list':in_patient_list,'regions':regions,'path':'home'})

def patient_searchs(request):
	search=request.POST['search']
	hospital_id=request.POST['hospital_id']   
	search_result=patient_search(search,hospital_id)
	data_list=[]
	print(search_result)
	for results in search_result:
		print(results['patient__card_number'])
		fullname=results['patient__First_Name']+" "+results['patient__Last_Name']
		data_list.append({'fullname':fullname,'dob':results['patient__Date_Of_Birth'],'telephone':results['patient__Telephone'],'patient_id':results['patient__card_number'],'total_visit':results['total_visit'],'patient_history_id':results['patient__id']})
	return JsonResponse({'result':data_list})

def create_patient(request):
	first_name=request.POST['first_name']
	last_name=request.POST['last_name']
	date_of_birth=request.POST['dob']
	telephone=request.POST['phone']
	region=request.POST['region']
	town=request.POST['town']
	hospital_id=request.POST['hospital_id']
	user_id=request.POST['user_id']
	print('am here ',first_name,last_name,date_of_birth,telephone,region,town)
	create_patients=patient(first_name,last_name,date_of_birth,telephone,region,town,hospital_id,user_id)
	print(create_patients)
	
	status_type=""
	msg=""
	if create_patients == True:
		status_type+="success"
		msg+="patient details created successfully"
	else:
		status_type+="error"
		msg+="couldn't patient details"
	return JsonResponse({'status':status_type,status_type:msg})

def view_patient_detail(request,patient_card_id):
	patients_details=view_patient_details(patient_card_id)
	details=[]
	for patients in patients_details:
		fullname=patients['patient__First_Name']+" "+patients['patient__Last_Name']
		details.append({'fullname':fullname,'dob':patients['patient__Date_Of_Birth'],'phone':patients['patient__Telephone'],'region':patients['patient__region__region'],'City':patients['patient__Town'],'visit':patients['total_visit']})

	patient_opd_history=paitient_opd_visiting_history(patient_card_id)
	return render(request,'dashboard/patients/view-paitent-details.html',{'title':'Views Patient Details','view_patient_details':details,'pateint_opd_history':patient_opd_history}) 

def view_patient_visitng_history(patient_id):
	pass

def view_opd_vitals(request):
	#this page is for only admin for viewing, creating and editing opd vitals
	opd_vital=opd_vitals()
	#print(opd_vital)
	#print('we are here')
	return render(request,'dashboard/patients/view-opd-vital-list.html',{'title':'OPD Panel','opd_vitals':opd_vital})
def create_opd_vital(request):
	#create opd vitals
	vitals_list=['temperature','weight','blood pressure']
	opd=create_opd_vitals(vitals_list)
	status_type=""
	msg=""
	if opd == True:
		status_type+="success"
		msg+="patient details created successfully"
	else:
		status_type+="error"
		msg+="Couldn't create opd vital"
	return JsonResponse({'status':status_type,status_type:msg})

def edit_opd_details(request):
	#edit opd vitals
	vital="BP"
	vital_id="3"
	edit_details=edit_opd_vitals(vital_id,vital)
	status_type=""
	msg=""
	if edit_details == True:
		status_type+="success"
		msg+="opd vitals edited"
	else:
		status_type+="error"
		msg+="couldn't create opd vitals"

	return JsonResponse({'status':status_type,status_type:msg})

def waiting_patient_list(request):
	#can only be view by admin and doctor
	waiting_patient=patinet_waiting_list()
	return render(request,'dashboard/patients/medicals-patients-waiting.html',{'title':'waiting patient list','waiting_list':waiting_patient})
def patient_medical_history_search(request):
	search=request.POST['patient_medical_history']
	hospital_id=request.POST['hospital_id']   
	search_result=Check_in_patient_search(search,hospital_id)
	data_list=[]
	print(search_result)
	for results in search_result:
		
		fullname=results['patient_history__patient__First_Name']+" "+results['patient_history__patient__Last_Name']
		data_list.append({'fullname':fullname,'dob':results['patient_history__patient__Date_Of_Birth'],'telephone':results['patient_history__patient__Telephone'],'patient_id':results['patient_history__patient__card_number'],'total_visit':results['total_visit'],'patient_history_id':results['patient_history__id']})
	return JsonResponse({'result':data_list})

def patient_profile(request,patient_history_id):
	#admin will have acces but cannot create or edit
	#doctors will have accces to write and edit
	'''
     1.taken patient opd details
     2.paitent_complient
     3.doctor diagnosis
     4. lab request
     5.pharmacy request
	'''
	#get patients bio
	check_details=patient_history_details(patient_history_id)
	patient_record_details=view_patient_details(check_details.patient.card_number)
	patient_medical_records=patient_medical_diagnosis_records(check_details.patient.id)


	details=[]
	for patients in patient_record_details:
		fullname=patients['patient__First_Name']+" "+patients['patient__Last_Name']
		details.append({'fullname':fullname,'dob':patients['patient__Date_Of_Birth'],'phone':patients['patient__Telephone'],'region':patients['patient__region__region'],'City':patients['patient__Town'],'visit':patients['total_visit']})

	#patient opd reports
	
	
	patient_opd_vital=view_paitent_opd_reports(patient_history_id)
	
	#opd vital details
	opd_vital=opd_vitals()
	#patient medical complainent
	patient_complaints=view_patient_diagnosis_complaints(patient_history_id)


	#view laboratory test list
	lab_test_lists=view_lab_test_list()
	#print(lab_test_lists)

	#patient_lab_test_details
	patient_lab_test_status=view_patient_lab_report_status(patient_history_id)
	
	#view dietary
	patient_dietry_details=patient_dietary_status(patient_history_id)

	#view dietry list
	dietary_lists=view_dietary_list()
	print(patient_medical_records)
	return render(request,'dashboard/patients/patient-profile.html',{'title':'patient profile','patient_opd_vital':patient_opd_vital,'opd_vital':opd_vital,'patient_lab_test_status':patient_lab_test_status,'lab_test_lists':lab_test_lists,'patient_dietary_status':patient_dietry_details,'dietary_lists':dietary_lists,'patient_history_id':patient_history_id,'patient_complaints':patient_complaints,'patient_details':details,'patient_medical_records':patient_medical_records})


def create_patient_complaints_diagonsis(request):
	patient_history_id=request.POST['patient_history_id']
	user_id=request.POST['user_id']
	patient_complaints=request.POST['complaints'].strip()
	status_type=""
	msg=""
	create_complaints_diagnosis=patient_diagonsis_history(patient_history_id,patient_complaints,user_id)

	if create_complaints_diagnosis == True:
		status_type+="success"
		msg+="patient complains submitted"

	else:
		status_type+="error"
		msg+="couldn't submit patient complains"

	return JsonResponse({'status':status_type,status_type:msg})


def create_patient_opd_vitals(request):
	patient_history_id = request.POST.get('patient_history_id',False)
	vital_id=request.POST.getlist('vital_id')
	vital_details=request.POST.getlist('vital')	  
	patient_opd_history=patient_opd_history_vitals(patient_history_id,vital_id,vital_details)
	status_type=""
	msg=""
	if patient_opd_history == True:
		status_type+="success"
		msg+="patient opd vitals details created successfully"
	else:
		status_type+="error"
		msg+="couldn't create patient details"
	return JsonResponse({'status':status_type,status_type:msg})
	  



def edit_doctor_diagonsis(request):
	patient_diagnosis_id=request.POST['diagnosis_id']
	diagnosis=request.POST['doctor_diagonsis'].strip()
	diagnosis_test=doctor_diagonsis(patient_diagnosis_id,diagnosis)
	msg=""
	status_type=""
	if diagnosis_test == True:
		status_type+="success"
		msg+="paitent diagnosis details submitted"
	else:
		status_type+="error"
		msg+="couldn't create patient diagnosis details"
	return JsonResponse({'status':status_type,status_type:msg})
def patient_medical_history_records(request):
	return render(request,'dashboard/patients/patient-diagnosis-medical-history.html',{'title':'patient medical history'.upper()})
def create_patient_lab_request(request):
	patient_id=request.POST['patient_history_id']

	patient_history=getPatientDiagnosisId(patient_id)
	patient_diagnosis_id=""
	print('patient details',patient_history)
	for patient in patient_history:
		print('go id',patient.id)
		patient_diagnosis_id+=str(patient.id)
	#print(patient_diagnosis_id)
	#return JsonResponse({'status':'hello'})

	
	user_id=request.POST.get('user_id')
	test_type=request.POST.getlist('lab_test')
	
	


	lab_request=send_lab_request(patient_diagnosis_id,user_id,test_type)
	msg=""
	status_type=""
	if lab_request == True:
		status_type+="success"
		msg+="paitent lab details request submited"
	else:
		status_type+="error"
		msg+="couldn't send patient request lab"
	
	return JsonResponse({'status':status_type,status_type:msg})
	

def create_patient_dietary_request(request):
	patient_id=request.POST['patient_history_id']
	patient_history=getPatientDiagnosisId(patient_id)
	user_id=request.POST.get('user_id')
	dietary_list=request.POST.getlist('dietary')
	patient_diagnosis_id=""
	for patient in patient_history:
		patient_diagnosis_id+=str(patient.id)

	dietary_request=send_dietary_request(patient_diagnosis_id,user_id,dietary_list)
	msg=""
	status_type=""
	if dietary_request == True:
		status_type+="success"
		msg+="paitent dietary details request submited"
	else:
		status_type+="error"
		msg+="couldn't send patient dietary request details"
	return JsonResponse({'status':status_type,status_type:msg})	

def view_patient_lab_test(request,patient_history_id):

    pass
def request_patient_lab(request):
	pass




'''
laboratory test setup

'''

def view_lab_test_types(request):
	#only to be viewed by the lab technician and admin
	'''
     this allows for the creation of lab test and it details
     view lab test and also edit lab test
	'''
	lab_test_lists=view_lab_test_list()
	return render(request,'dashboard/laboratory/lab-test.html',{'title':'Lab test list','lab_test':lab_test_lists})

def create_lab_test_types(request):
	lab_test=request.POST['test']
	cost=request.POST['cost']
	notes=request.POST['notes']
	lab_test_cost=create_lab_test_details_cost(lab_test,notes,cost)
	msg=""
	status_type=""
	if lab_test_cost == True:
		status_type+="success"
		msg+="lab test created successfully"
	else:
		status_type+="error"
		msg+="couldn't create lab test types. Test Details already exist"
	return JsonResponse({'status':status_type,status_type:msg})	


def edit_lab_test_type(request):
	lab_test=request.POST['test']
	notes=request.POST['notes']
	cost=request.POST['cost']
	lab_id=request.POST['id']
	edit_lab_test=edit_lab_test_list_details(lab_test,notes,cost,lab_id)
	msg=""
	status_type=""

	if edit_lab_test == True:
		status_type+="success"
		msg+="lab test edited successfully"

	else:
		status_type+="error"
		msg+="couldn't edit lab test types. "
	return JsonResponse({'status':status_type,status_type:msg})



def view_lab_tests_request(request):
	'''
	  list of all patient taking lab test
	'''
	lab_test_list=view_lab_test_list()
	view_patient_lab_request=view_lab_test_request()
	return render(request,'dashboard/laboratory/patients-lab-test-request.html',{'title':'Patient Lab test request','view_patient_lab_request':view_patient_lab_request,'test_list':lab_test_list})

def search_patient_lab_records(request):
	search=request.POST['patient_lab_record']
	hospital_id=request.POST['hospital_id']   
	search_result=lab_patient_search(search,hospital_id)
	data_list=[]
	
	for results in search_result:
		
		fullname=results['patient_history__patient__First_Name']+" "+results['patient_history__patient__Last_Name']
		data_list.append({'fullname':fullname,'dob':results['patient_history__patient__Date_Of_Birth'],'telephone':results['patient_history__patient__Telephone'],'patient_id':results['patient_history__patient__card_number'],'total_visit':results['total_visit'],'patient_history_id':results['patient_history__id']})
	return JsonResponse({'result':data_list})
def view_patient_required_lab_test(request,patient_history_id):
    #lat updates
	check_details=patient_history_details(patient_history_id)
	patient_record_details=view_patient_details(check_details.patient.card_number)
	patient_lab_record=patient_laboratory_records_history(check_details.patient.id)
	details=[]
	for patients in patient_record_details:
		fullname=patients['patient__First_Name']+" "+patients['patient__Last_Name']
		details.append({'fullname':fullname,'dob':patients['patient__Date_Of_Birth'],'phone':patients['patient__Telephone'],'region':patients['patient__region__region'],'City':patients['patient__Town'],'visit':patients['total_visit']})

	patient_lab_report_result(patient_history_id)
	patient_lab_history=view_patint_lab_history(patient_history_id)
	patient_lab_request_details=view_patient_lab_details(patient_history_id)
	return render(request,'dashboard/laboratory/patient-lab-details.html',{'title':'patient lab history','patient_lab_history':patient_lab_history,'lab_request':patient_lab_request_details,'patient_history_id':patient_history_id,'patient_lab_history_record':patient_lab_record,'patient_bio':details})
   #view vital test to be taken
   #view patient test history
   #enter test results and relaese test results

  
def input_lab_test_result_details(request):
	lab_test_id=request.POST.getlist('lab_id')
	patient_lab_test_id=request.POST.getlist('patient_lab_id')
	lab_test_details=request.POST.getlist('lab_test_details')
	patient_history_id=request.POST['patient_history_id']
	print('supt ',request.POST['patient_history_id'])
	input_result=input_patient_lab_request(patient_lab_test_id,lab_test_id,lab_test_details,patient_history_id)
	
	msg=""
	status_type=""
	if input_result == True:
		status_type+="success"
		msg+="lab test input successfull"
	else:
		status_type+="error"
		msg+="couldn't input lab test result"
	return JsonResponse({'status':status_type,status_type:msg})	

def view_paitent_lab_history(request):
	pass

'''
   patient dietary
'''
def view_dietary(request):
    pass
def view_dietary_stock(request):
	pass
def create_inventary_dietary_stock(request):
	dietary=request.POST['dietary']
	notes=request.POST['notes']
	cost=request.POST['price']
	quantity_stocked=int(request.POST['quantity'])
	user_id=request.POST['user_id']
	photo=request.FILES['photo']
	lab_test_cost=create_dietary_supplementary_cost(dietary,notes,cost,quantity_stocked,photo,user_id)
	msg=""
	status_type=""
	if lab_test_cost == True:
		status_type+="success"
		msg+="dietary stock successfully"
	else:
		status_type+="error"
		msg+="couldn't create dietary supplementary stock. Details already exists"
	return JsonResponse({'status':status_type,status_type:msg})	

def edit_dietary_inventory_stock(request):
	pass

def view_patient_dietary_lists(request):
	patient_dietary_list=view_dietary_pending_list()
	return render(request,"dashboard/dietary/patient-dietary-list.html",{'title':'Patient Dietary','patient_dietary_list':patient_dietary_list})

def view_patient_dietary_details(request,patient_history_id):
	print('hello ',patient_history_id)
	patient_deitary_details=view_patient_deietary_details(patient_history_id)
	return render(request,'dashboard/dietary/patient-dietary.html',{'title':'Patient Dietary Details','patient_dietry_details':patient_deitary_details,'patient_history_id':patient_history_id})

def dispen_patient_dietary(request):
	patient_dietary_id=request.POST.getlist('patient_dietary_id')
	dietary_id=request.POST.getlist('dietary_id')
	dispensed_status=True 
	quantity=request.POST.getlist('dietary_quantiy')
	patient_history_id=request.POST['patient_history_id']

	dispense_dietary=input_patient_dietry_request(patient_dietary_id,dietary_id,dispensed_status,quantity,patient_history_id)
	msg=""
	status_type=""
	if dispense_dietary == True:
		status_type+="success"
		msg+="dietary dispensed successfully"
	else:
		status_type+="error"
		msg+="couldn't dispensed dietary successfully"
	return JsonResponse({'status':status_type,status_type:msg})	








def staff_management(request):
	'''
         admin only
	'''
	get_groups=Group.objects.all()
	all_staffs=view_all_staffs()

	return render(request,'dashboard/setting/staff-management.html',{'title':'staff management','groups':get_groups,'staffs':all_staffs})

def staff_user_management(request,staff_id):
	staff_details=Hospital_Staff.objects.get(pk=staff_id)
	user_groups=request.user.groups.filter(user__id=staff_details.staff.id)
	print(user_groups)
	return render(request,'dashboard/setting/staff-user-management.html',{'title':'staff management','staff_details':staff_details})


def user_management(request):
	return render(request,'dashboard/setting/user-management.html',{'title':'staff management'})
def laboratory_management(request):
	lab_test_lists=view_lab_test_list()
	return render(request,'dashboard/setting/Laboratory-management.html',{'title':'Laboratory Management','lab_test':lab_test_lists})

def laboratory_test_management_details(request,lab_test_id):
	laboratory_test=getLaboratory(lab_test_id)
	return render(request,'dashboard/setting/Laboratory-test-details.html',{'title':'Laboratory Test Management Details','lab_details':laboratory_test})


def dietary_stocking(request):
	dietary_list=view_dietary_list()
	restock_dietary=dietary_need_restock()
	return render(request,'dashboard/setting/dietary-stock.html',{'title':'Dietary Supplement Stocking','dietary':dietary_list,'restock':restock_dietary})
def dietary_stocking_view(request,dietary_id):
	dietary_supplement_stock=dietary_supplement_stocking_details_history(dietary_id)
	dietary_supplement_stock_details=deitary_stock_info(dietary_id)
	return render(request,'dashboard/setting/dietary-stock-view-edit.html',{'title':'dietary stocking history','dietary_stock':dietary_supplement_stock,'dietary_id':dietary_id,'dietary_details':dietary_supplement_stock_details})

def company(request):
	region=Region.objects.all()

	return render(request,'dashboard/setting/company.html',{'title':'comapny agadarko','Region':region})







'''
           stocking updates
'''



def update_dietary_inventary_stock(request):
	price=request.POST['price']
	quantity=request.POST['quantity']
	user_id=request.POST['user_id']
	dietary_id=request.POST['dietary_id']

	stock_update=update_dietary_details_stock(dietary_id,quantity,price,user_id)
	msg=""
	status=""
	if stock_update == True:
		status+="success"
		msg+='dietary supplement stock update succefull'
	else:
		status+="error"
		msg+="couldn't update dietary supplement"
	return JsonResponse({'status':status,status:msg})
def update_dietary_supplement_details(request):
	dietary=request.POST['dietary']
	notes=request.POST['notes'].strip()
	dietary_id=request.POST['dietary_id']
	update_dietary=update_dietary_details(dietary_id,dietary,notes)
	msg=""
	status=""	
	if update_dietary == True:
		status+="success"
		msg+='dietary supplements details update successfull'
	else:
		status+="error"
		msg+="couldn't update dietary supplement details"		

	return JsonResponse({'status':status,status:msg})

def set_hospital_details(request):
	hospital_name=request.POST['company_name']
	user=request.POST['user']
	email=request.POST['email']
	telephone=request.POST['telephone']
	town=request.POST['town']
	region=request.POST['region']
	msg=""
	status=""
	create_hospital=create_hospital_details(hospital_name,user,email,telephone,town,region)
	print(create_hospital)
	if create_hospital == True:
		status+="success"
		msg+='hospital details created successfully'
	else:
		status+="error"
		msg+="couldn't create hospital details. Hospital Details already exist"
	return JsonResponse({'status':status,status:msg})
def create_staff_details(request):
	first_name=request.POST['fname']
	last_name=request.POST['lname']
	mail=request.POST['email']
	username=request.POST['username']
	telephone=request.POST['phone']
	group=request.POST.getlist('group')
	user_id=request.POST['user_id']
	staffs=create_staff(first_name,last_name,mail,username,telephone,group,user_id)
	msg=""
	status=""
	if staffs == True:
		status+="success"
		msg+='staff account created successfully'
	else:
		status+="error"
		msg+="couldn't create staff account. Staff account already exist"
	return JsonResponse({'status':status,status:msg})

def staff_update(request):
	first_name=request.POST['fname']
	last_name=request.POST['lname']
	mail=request.POST['email']
	username=request.POST['username']
	telephone=request.POST['phone']
	user_id=request.POST['staff_id']
	hospital_staff_id=request.POST['staff_hospital_id']

	create_staff=edit_staff(mail,first_name,last_name,username,telephone,user_id,hospital_staff_id)
	msg=""
	status=""
	if create_staff == True :
		status+="success"
		msg+='staff account updated successfully'
	else:
		status+="error"
		msg+="couldn't update staff account."
	return JsonResponse({'status':status,status:msg})


def change_pass(request):
	password=request.POST['new_password']
	confirm_password=request.POST['retype_new_password']
	user_id=request.POST['staff_id']
	change_pasword=change_staff_password(password,confirm_password,user_id)
	status=""
	msg=""	
	if change_pasword == True:
		status+="success"
		msg+='password changed successfully'
	else:
		status+="error"
		msg+="couldn't change staff_password ! password mismatch"	
	return JsonResponse({'status':status,status:msg})		


def multiple_dietary_supplement_list(request):
	dietary_list=request.GET.getlist('choose')
	lists=list()
	for items in dietary_list:
		data=json.loads(items)
		lists.append(data)
	diet=multiple_dietary_list(data)
	
	return JsonResponse({'status':diet})

def multiple_lab_test_list(request):
	dietary_list=request.GET.getlist('choose')
	lists=list()
	for items in dietary_list:
		data=json.loads(items)
		lists.append(data)
	diet=multiple_lab_type_list(data)
	
	return JsonResponse({'status':diet})



