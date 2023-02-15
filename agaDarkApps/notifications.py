from .models import Patient_History,Patient_Diagosis_History,Patient_Laboratory,Patient_Dietary


def checkin_in_patient_for_herbal_care():
	return Patient_History.objects.filter(checked_in=True,checked_out=False)

def medical_care_lab_request():
	return Patient_Diagosis_History.objects.filter(laboratory_report_request_status=True,laboratory_report_recieved_status=False)

def lab_test_released_to_herbal_care():
	return Patient_Laboratory.objects.filter(released_status=True,viewed_status=True)
def medical_request_to_dietary():
	pass