from .models import Patient_History,Patient_Diagosis_History,Patient_Laboratory,Patient_Dietary,OPD_Charges,OPD_Payment_Charges,OPD_Charges_Updates
from django.db.models import Count ,F,Q,Sum
from django.db.models.functions import LPad 

def creat_update_opd_charges(first_charge,second_charge,user_id):
	check_charges=OPD_Payment_Charges.objects.all().count()
	charges=OPD_Payment_Charges.objects.all()[0]
	if check_charges == 1:
		 #update data in OPD_Charges table and OPD_Charges_Updates
		 new_charges=OPD_Payment_Charges.objects.get(pk=charges.id)
		 new_charges.first_time_charge=first_charge
		 new_charges.second_time_charge=second_charge
		 new_charges.save()
		 updates_opd_charges(first_charge,second_charge,user_id)
	elif check_charges ==0:
		#inserting data into OPD_Charges table and OPD_Charges_Updates
		new_charges=OPD_Payment_Charges.objects.create(first_time_charge=first_charge,second_time_charge=second_charge)
		new_charges.save()
		updates_opd_charges(first_charge,second_charge,user_id)
		 

def patient_opd_payment_charges(patient_id,patient_history_id,amount,user_id):
	patient_record_details=Patient_History.objects.filter(patient__id=patient_id).count()
	patient_record=Patient_History.objects.get(pk=patient_history_id)
	charges=OPD_Payment_Charges.objects.all()[0]
	if patient_record_details > 1:
		#pay second charge
		if amount == second_charge.second_time_charge:
			payments=make_payment(patient_history_id,amount,user_id)
			patients_checked_in(patient_id)
			return payments
		else:
			return False


	elif patient_record_details == 1 :
		if amount == second_charge.first_tim3_charge:
		    payments=make_payment(patient_history_id,amount,user_id)
		    patients_checked_in(patient_id)
		    return payments
		else:
			return False
	else:
		return False
def patients_checked_in(patient_id):
	get_patient=Patient.objects.get(pk=patient_id)
	get_patient.waiting_state="checked in"
	get_patient.save()
def make_payment(patient_history_id,amount,user_id):
	payment=OPD_Payment_Charges.objects.create(patient_history=Patient_History.objects.get(pk=patient_history_id),amount_paid=amount,receiver=User.objects.get(pk=user_id))
	payment.save()
	payment_id=payment.latest('id')
	paym=payment_receipts(payment_id)
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
	check_in_status=Patient_History.objects.get(pk=patient_history_id)
	check_in_status.checked_in=True
	check_in_status.waiting_state='checked in'
	return True


def checked_out(patient_history_id):
	checked_out_status=Patient_History.objects.get(pk=patient_history_id)
	checked_out_status.checked_out=True
	checked_out_status.waiting_state='checked out'
	checked_out_status.save()
	return True



