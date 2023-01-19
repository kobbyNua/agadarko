from django.contrib.auth.models import User,auth,Group
from django.db.models import Count ,F,Q,Sum
from .models import Patient,Patient_History,OPD_Vitals,Patient_History_OPD_Vitals_Details,Patient_Diagosis_History,Region,Hospital,Patient_Laboratory,Patient_Dietary
from .laboratory import view_patient_lab_details,patient_lab_test_status,patient_laboratory
from .dietary import patient_dietary, view_patient_dietary_status,view_patient_deietary_details
from datetime import datetime

'''
stage 2
'''

'''
  search for patient details
'''
def  patient_search(searchs,hospital_id):
	return Patient_History.objects.values('patient__First_Name','patient__Last_Name','patient__Date_Of_Birth','patient__Telephone','patient__card_number','patient__id').filter(Q(patient__First_Name=searchs)|Q(patient__Last_Name=searchs)|Q(patient__Telephone=searchs),hospital__id=hospital_id).annotate(total_visit=Count('patient__id')).order_by()


'''
view patient details
'''
def view_patient_details(patient_card_id):
	patient_detail=Patient_History.objects.values('patient__First_Name','patient__Last_Name','patient__Date_Of_Birth','patient__Telephone','patient__card_number','patient__id','patient__Town','patient__region__region').filter(patient__card_number=patient_card_id).annotate(total_visit=Count('patient__id'))
	return patient_detail


def paitient_opd_visiting_history(card_id):
	return Patient_History.objects.filter(patient__card_number=card_id)
'''
create patients
'''
def getRegion():
	return Region.objects.all()
def  patient(first_name,last_name,date_of_birth,telephone,region,town,hospital_id,user_id):
	
	check_patient_details=Patient.objects.filter(First_Name=first_name,Last_Name=last_name,Telephone=telephone,Date_Of_Birth=date_of_birth)
	if not check_patient_details.exists():
		total_number_of_patient=Patient.objects.all().count()
		#count=0
		print(total_number_of_patient)
		if total_number_of_patient == 0:
			total_number_of_patient+=1
			patient_card_number=str(total_number_of_patient)+'-'+str(datetime.now().year)
			print(patient_card_number)
		else:
			patient_card_number=str(total_number_of_patient)+'-'+str(datetime.now().year)
			#return patient_card_number
		unit_number='A.G.D-'+patient_card_number
		registration_number=patient_card_number
		print(registration_number)
		date_format="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
		register_patient=Patient.objects.create(First_Name=first_name,Last_Name=last_name,Date_Of_Birth=date_of_birth,Telephone=telephone,region=Region.objects.get(pk=region),Town=town,card_number=patient_card_number,unit_no=unit_number,registration_number=registration_number,registered_by=User.objects.get(pk=user_id),date_registered=date_format)
		register_patient.save()
		patient_id=Patient.objects.latest('id')
		create_patient_history=patient_history(patient_id.id,hospital_id,user_id)
		print(create_patient_history)
		return create_patient_history		
	else:
		return False


def  patient_history(patient_id,hospital_id,user_id):
	
	date_formated=datetime.now()
	date_format="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
	print(date_format)
	create_patient_history=Patient_History.objects.create(patient=Patient.objects.get(pk=patient_id),hospital=Hospital.objects.get(pk=hospital_id),nurse=User.objects.get(pk=user_id),date_reported=date_format,checked_in=True)
	create_patient_history.save()
	return True



def checked_out(patient_history_id):
	checked_out_status=Patient_History.objects.get(pk=patient_history_id)
	checked_out_status.checked_out=False
	checked_out_status.save()


'''
  stage 3
  doctor and nurse functions
'''
def opd_vitals():
	return OPD_Vitals.objects.all()
def  create_opd_vitals(opd):
	for items in range(len(opd)):
		vitals=OPD_Vitals.objects.create(vital_type=opd[items])
		vitals.save()
	return True
def edit_opd_vitals(vital_id,vitals):
	vital=OPD_Vitals.objects.get(pk=vital_id)
	vital.vital_type=vitals
	vital.save()
	return True
def patinet_waiting_list():
	  return Patient_History.objects.filter(waiting_state="waiting",checked_in=True,checked_out=False)

def patient_opd_history_vitals(patient_history_id,vitals,details):
	#print(details)
	for items in range(len(details)):

		opd_vital_history=Patient_History_OPD_Vitals_Details.objects.create(patient_history=Patient_History.objects.get(pk=patient_history_id),vitals=OPD_Vitals.objects.get(pk=vitals[items]),details=details[items])
		opd_vital_history.save()
	return True

def view_paitent_opd_reports(patient_history_id):
	return Patient_History_OPD_Vitals_Details.objects.filter(patient_history__id=patient_history_id)

'''
def patient_opd_complaints_history(patient_history_id,complaint):
            pat_opd_vital_history=Patient_History_OPD_Vitals_History.objects.create(patient_history=Patient_History.objects.get(pk=patient_history_id),patient_complaint=complaint)
            pat_opd_vital_history.save()
'''

def view_patient_medical_history(patient_id):
	 pass
def view_patient_diagnosis_complaints(patient_history_id):
	return Patient_Diagosis_History.objects.filter(patient_history=patient_history_id)
def patient_diagonsis_history(patient_history_id,patient_narratives,user_id):
	date_formated=datetime.now()
	date_format="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
	patient_diagonsis=Patient_Diagosis_History.objects.create(patient_history=Patient_History.objects.get(pk=patient_history_id),patient_complaint=patient_narratives,doctor=User.objects.get(pk=user_id),date_diagosed=date_format)
	patient_diagonsis.save()
	return True
def doctor_diagonsis(patient_diagnosis_id,dignosis):
	get_patient_medical_diagnosis=Patient_Diagosis_History.objects.get(pk=patient_diagnosis_id)
	get_patient_medical_diagnosis.doctor_dignosis_report=dignosis
	get_patient_medical_diagnosis.save()
	return True

def getPatientDiagnosisId(patient_history_id):
	return Patient_Diagosis_History.objects.filter(patient_history__id=patient_history_id)

def send_lab_request(patinet_diagonsis_id,user_id,type_of_test):
	'''
	take patient diagonsis history id and update laboratory report request status field status to true
	and create take paitent labaroary details and return total cost
	'''
	patient_diagonsis_history=Patient_Diagosis_History.objects.get(pk=patinet_diagonsis_id)
	patient_diagonsis_history.laboratory_report_request_status=True
	patient_diagonsis_history.save()
	
	#print(patient_diagonsis_history.patient_history.id,patinet_diagonsis_id)
	lab_request=patient_laboratory(patient_diagonsis_history.patient_history.id,patinet_diagonsis_id,user_id,type_of_test)
	return lab_request

def patient_lab_report_result(patient_history_id):
	patient_digonosis_report=getPatientDiagnosisId(patient_history_id)
	patient_diagnosis_id=""
	for patient_diagonsis in patient_digonosis_report:
		patient_diagnosis_id+=str(patient_diagonsis.id)

	patient_lab=Patient_Laboratory.objects.get(patient_diagonsis_history_details__id=patient_diagnosis_id,patient_history__id=patient_history_id)
	patient_lab.viewed_status=True
	patient_lab.save()
	'''
	lab_status_id=""
	for lab_status in patient_lab:
		lab_status_id+=str(lab_status.id)
	patient_view_status_report=Patient_Laboratory.objects.get(pk=lab_status_id)
	patient_view_status_report.viewed_status=True
	
	'''
	return True

def send_dietary_request(patient_diagnosis_id,user_id,dietary_list):
	'''
        take patient diagonsis history id and update laboratory report request status field status to true
        and create take paitent labaroary details and return total cost
	'''
	patient_diagonsis_history=Patient_Diagosis_History.objects.get(pk=patient_diagnosis_id)
	patient_diagonsis_history.dietary_report_reuqest_status=True
	patient_diagonsis_history.save()
	dietary_request=patient_dietary(patient_diagonsis_history.patient_history.id,patient_diagnosis_id,user_id,dietary_list)
	return dietary_request
def patient_dietary_report_result(patient_history_id):
	patient_digonosis_report=getPatientDiagnosisId(patient_history_id)
	patient_diagnosis_id=""
	for patient_diagonsis in patient_digonosis_report:
		patient_diagnosis_id+=str(patient_diagonsis.id)
	patient_view_status_report=Patient_Dietary.objects.get(patient_diagonsis_history_details__id=patient_diagnosis_id)
	patient_view_status_report.viewed_status=True
	patient_view_status_report.save()


#0243391755
#0557091718

def view_patient_lab_test_report(patient_history_id):
	return view_patient_lab_details(patient_history_id)

def view_patient_lab_report_status(patient_history_id):
	return patient_lab_test_status(patient_history_id)


def patient_dietary_status(patient_history_id):
	return  view_patient_dietary_status(patient_history_id)

def ptient_dietary_deitary_report(patient_history_id):
	return view_patient_deietary_details(patient_history_id)


'''
   patient checked
'''
def patient_check_in_list():
	#display all in patient list
	return Patient_History.objects.filter(checked_in=True,checked_out=False)

def  Check_in_patient_search(searchs,hospital_id):
	return Patient_Diagosis_History.objects.values('patient_history__patient__First_Name','patient_history__patient__Last_Name','patient_history__patient__Date_Of_Birth','patient_history__patient__Telephone','patient_history__patient__card_number','patient_histor__id').filter(Q(patient_history__patient__First_Name=searchs)|Q(patient_history__patient__Last_Name=searchs)|Q(patient_history__patient__Telephone=searchs),hospital__id=hospital_id).annotate(total_visit=Count('patient_history__patient__id')).order_by()


