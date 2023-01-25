from .models import Patient_History,Patient,Patient_Diagosis_History,Patient_Laboratory,Patient_Dietary,OPD_Charges,OPD_Payment_Charges,OPD_Charges_Updates
from django.db.models import Count ,F,Q,Sum,Value
from django.db.models.functions import LPad 
from django.contrib.auth.models import User,auth,Group

def creat_update_opd_charges(first_charge,second_charge,user_id):
	check_charges=OPD_Charges.objects.all().count()
	charges=OPD_Charges.objects.all()[0]
	if check_charges == 1:
		 #update data in OPD_Charges table and OPD_Charges_Updates
		 new_charges=OPD_Charges.objects.get(pk=charges.id)
		 new_charges.first_time_charge=first_charge
		 new_charges.second_time_charge=second_charge
		 new_charges.save()
		 updates_opd_charges(first_charge,second_charge,user_id)
	elif check_charges == 0:
		#inserting data into OPD_Charges table and OPD_Charges_Updates
		new_charges=OPD_Charges.objects.create(first_time_charge=first_charge,second_time_charge=second_charge)
		new_charges.save()
		updates_opd_charges(first_charge,second_charge,user_id)
		 

def patient_opd_payment_charges(patient_id,patient_history_id,amount,user_id):
	patient_record_details=Patient_History.objects.filter(patient__id=patient_id).count()
	patient_record=Patient_History.objects.get(pk=patient_history_id)
	charges=OPD_Charges.objects.all()[0]
	if patient_record_details > 1:
		#pay second charge
		if flaot(amount) == charges.second_time_charge:

			payments=make_payment(patient_history_id,amount,user_id)
			if payments == True:
				new_sessions=patients_checked_in(patient_id)
				return new_sessions
			
		else:
			return False


	elif patient_record_details == 1 :
	
		if float(amount) == charges.first_time_charge:
		
			payments=make_payment(patient_history_id,amount,user_id)
			if payments == True:
				new_sessions=patients_checked_in(patient_id)
				return new_sessions
		else:
			return False
			
	else:
		return False
def patients_checked_in(patient_id):
	get_patient=Patient.objects.get(pk=patient_id)
	get_patient.waiting_state="checked in"
	get_patient.save()
	return True
def make_payment(patient_history_id,amount,user_id):
	payment=OPD_Payment_Charges.objects.create(patient_history=Patient_History.objects.get(pk=patient_history_id),amount_paid=amount,receiver=User.objects.get(pk=user_id))
	payment.save()
	payment_id=OPD_Payment_Charges.objects.latest('id')
	paym=payment_receipts(payment_id.id)
	if paym == True:
		check_in=check_in_patient(patient_history_id)
		return check_in

def payment_receipts(payment_id):
	payments=OPD_Payment_Charges.objects.get(pk=payment_id)
	payments.recepit=LPad('id',6,Value('0'))
	payments.save()
	return True
def updates_opd_charges(first_charge,second_charge,user_id):
	new_updates=OPD_Charges_Updates.objects.create(updated_by=user_id,first_time_old_charge=first_charge,second_time_old_charge=second_charge)
	new_updates.save()
	return True

def check_in_patient(patient_history_id):
	print('am here',patient_history_id)
	check_in_status=Patient_History.objects.get(pk=patient_history_id)
	check_in_status.checked_in=True
	check_in_status.waiting_state='checked in'
	check_in_status.save()
	return True


def checked_out(patient_history_id):
	checked_out_status=Patient_History.objects.get(pk=patient_history_id)
	checked_out_status.checked_out=True
	checked_out_status.waiting_state='checked out'
	checked_out_status.save()
	return True






def current_registration_charges():
	return OPD_Charges.objects.all()

def registration_payment_history():
	return OPD_Charges_Updates.objects.all()

def patient_payment_list():
	details=[]
	patient_history_records=Patient_History.objects.all()
	for patients in patient_history_records:

		patient_laboratory_records=Patient_Laboratory.objects.filter(patient_history__id=patients.id,released_status=True)
		patient_dietary_records=Patient_Dietary.objects.filter(patient_history__id=patients.id,released_status=True)
		if patient_laboratory_records.exists() and patient_dietary_records.exists():
			get_patient_laboratory_records=Patient_Laboratory.objects.get(patient_history__id=patients.id,released_status=True)

			get_patient_dietary_records=Patient_Dietary.objects.get(patient_history__id=patients.id,released_status=True)
			fullname = patients.patient.First_Name+" "+patients.patient.Last_Name
			details.append({'fullname':fullname,'patients_card':patients.patient.card_number,'case_number':patients.case_number,'lab_total_cost':get_patient_laboratory_records.total_cost,'dietary_total_cost':get_patient_dietary_records.total_cost})

	return details


def payment_trakings(patient_history_id):
	payments=OPD_Payment_Charges.objects.filter(patient_history__case_number=patient_history_id)
	if payments.exists():
		return True
	else:
		return False

def payment_trakings_history(patient_history_id):
	patient_history_records=Patient_History.objects.get(case_number=patient_history_id)
	return OPD_Payment_Charges.objects.filter(patient_history__id=patient_history_records.id)