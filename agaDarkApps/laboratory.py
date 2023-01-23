from django.contrib.auth.models import User,auth,Group
from django.db.models import Count ,F,Q,Sum
from .models import Lab_Test_Cost_Details,Patient_Laboratory,Patient_Laboratory_Details,laboratory_test_techician,Patient_Laboratory_Date_Released,Patient_History,Patient_Diagosis_History
from datetime import datetime


'''
  stage 4
'''
def view_lab_test_list():
	return Lab_Test_Cost_Details.objects.all()

def getLaboratory(test_id):
	return Lab_Test_Cost_Details.objects.get(pk=test_id)
def create_lab_test_details_cost(test_type,notes,cost):
	check_lab_test=Lab_Test_Cost_Details.objects.filter(test_type=test_type)
	if not check_lab_test.exists():
			create_lab_test_list=Lab_Test_Cost_Details.objects.create(test_type=test_type,notes=notes,cost=cost)
			create_lab_test_list.save()		
			return True
	else:
		  return False

def edit_lab_test_list_details(test_type,notes,cost,test_id):
	get_lab_test=Lab_Test_Cost_Details.objects.get(pk=test_id)
	get_lab_test.test_type=test_type
	get_lab_test.notes=notes
	get_lab_test.cost=cost
	get_lab_test.save()
	return True

def patient_laboratory(patient_history_id,patinet_diagonsis_id,user_id,test_type):
	date_format="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
	patient_laboratory_history=Patient_Laboratory.objects.create(patient_history=Patient_History.objects.get(pk=patient_history_id),patient_diagonsis_history_details=Patient_Diagosis_History.objects.get(pk=patinet_diagonsis_id),date_reported=date_format)
	patient_laboratory_history.save()
	patient_laboratory_id=Patient_Laboratory.objects.latest('id')
	status_state=""
	technician_who_handle_laboratory=laboratory_test_techician.objects.create(patient_laboratory=Patient_Laboratory.objects.get(pk=patient_laboratory_id.id),techinician=User.objects.get(pk=user_id))
	for lab_test in range(len(test_type)):
		#print('tests',test_type[tests])
		patient_lab_test_type_details=Patient_Laboratory_Details.objects.create(patient_laboratory=Patient_Laboratory.objects.get(pk=patient_laboratory_id.id),lab_test_type=Lab_Test_Cost_Details.objects.get(pk=test_type[lab_test]))
		patient_lab_test_type_details.save()
		patient_lab_test_cost_details(patient_laboratory_id.id,test_type)
	return True
def patient_lab_test_status(patient_history_id):
	get_patient=Patient_Laboratory.objects.filter(patient_history__id=patient_history_id)
	if get_patient.exists():
	    return Patient_Laboratory.objects.get(patient_history__id=patient_history_id)

def view_lab_test_request():
	return Patient_Laboratory.objects.filter(patient_diagonsis_history_details__laboratory_report_request_status=True,patient_history__checked_in=True,patient_history__checked_out=False)

def view_patient_lab_details(patient_history_id):
	return Patient_Laboratory_Details.objects.filter(patient_laboratory__patient_history__id=patient_history_id)

def input_patient_lab_request(patient_lab_details_id,lab_test_type_id,lab_test_details,patient_history_id):
	get_laboratory_id=Patient_Laboratory_Details.objects.filter(patient_laboratory__patient_history=patient_history_id)[0]
	for items in range(len(patient_lab_details_id)):
		input_patient_lab_details=Patient_Laboratory_Details.objects.get(pk=patient_lab_details_id[items],lab_test_type__id=lab_test_type_id[items])
		input_patient_lab_details.lab_test_status_report=lab_test_details[items]
		#print('prints: ',input_patient_lab_details.patient_laboratory.id)
		#patient_lab_details_id+=str(input_patient_lab_details.patient_laboratory.id)
		#input_patient_lab_details.patient_laboratory.patient_diagonsis_history_details.laboratory_report_recieved_status=True
		input_patient_lab_details.save()
		#patient_lab_details_id=Patient_Laboratory_Details.objects.get(pk=patient_lab_details_id[items],lab_test_type__id=lab_test_type_id[items])
	#print('tracking ',patient_lab_details_id)
	status_updates(get_laboratory_id.patient_laboratory.id)
	patient_diagnosis_status(get_laboratory_id.patient_laboratory.patient_diagonsis_history_details.id)
	#update_released_status=Patient_Laboratory.objects.get(pk)

	return True
def status_updates(patient_lab_id):
	patient_lab=Patient_Laboratory.objects.get(pk=patient_lab_id)
	patient_lab.released_status=True
	patient_lab.lab_report_status_seen=True
	#patient_diagnosis_status(patient_lab.patient_diagonsis_history_details.id)
	patient_lab.save()
def patient_diagnosis_status(patient_diagnosis_id):
	patient_diagnosis=Patient_Diagosis_History.objects.get(pk=patient_diagnosis_id)
	patient_diagnosis.laboratory_report_recieved_status=True
	#patient_diagnosis=True
	patient_diagnosis.save()
def view_patint_lab_history(patient_history_id):
     return Patient_Laboratory.objects.filter(patient_history__id=patient_history_id)

def released_test_result(patient_lab_id):
	'''
      connect the lab releaed date to input paitent lab request
	'''
	patient_laboratory_update=Patient_Laboratory.objects.get(pk=patient_lab_id)
	patient_laboratory_update.released_status=True 
	patient_laboratory_update.save()

def patient_lab_test_cost_details(patient_lab_id,test_type):
	total_cost=0
	
	for lab_test in range(len(test_type)):
		test_type_cost_details=Lab_Test_Cost_Details.objects.filter(id=test_type[lab_test])
		#details_list.append(test_type_cost_details)
		for test_cost in test_type_cost_details:
			total_cost+=test_cost.cost
	update_patient_lab_test_cost=Patient_Laboratory.objects.get(pk=patient_lab_id)
	update_patient_lab_test_cost.total_cost=total_cost
	update_patient_lab_test_cost.save()
	return True

def patient_laboratory_records_history(patient_id):
	return laboratory_test_techician.objects.filter(patient_laboratory__patient_history__patient__id=patient_id)


def multiple_lab_type_list(dietary_id):
	data=list()
	for items in dietary_id:
		lab=Lab_Test_Cost_Details.objects.get(pk=items)
		data.append({'items':lab.test_type,'amount':lab.cost})
	return data

def  lab_patient_search(searchs,hospital_id):
	return Patient_Laboratory.objects.values('patient_history__patient__First_Name','patient_history__patient__Last_Name','patient_history__patient__Date_Of_Birth','patient_history__patient__Telephone','patient_history__patient__card_number','patient_history__id').filter(Q(patient_history__patient__First_Name=searchs)|Q(patient_history__patient__Last_Name=searchs)|Q(patient_history__patient__Telephone=searchs),patient_history__hospital__id=hospital_id).annotate(total_visit=Count('patient_history__patient__id')).order_by()


def view_patient_laboratory_history_details(patient_card_id):
	patient_detail=Patient_Laboratory.objects.values('patient_history__patient__First_Name','patient_history__patient__Last_Name','patient_history__patient__Date_Of_Birth','patient_history__patient__Telephone','patient_history__patient__card_number','patient_history__patient__id','patient_history__patient__Town','patient_history__patient__region__region').filter(patient_history__patient__card_number=patient_card_id).annotate(total_visit=Count('patient_history__patient__id'))
	return patient_detail   


def get_patient_history_lab(lab_history_id):
	return Patient_Laboratory.objects.get(patient_history__id=lab_history_id)