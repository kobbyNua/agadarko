from .models import Patient_History,Patient_Diagosis_History,Patient_Laboratory,Patient_Dietary


def checkin_in_patient_for_herbal_care():
	return Patient_History.objects.filter(checked_in=True,waiting_state=True).count()

def medical_care_lab_request():
	return Patient_Diagosis_History.objects.filter(laboratory_report_request_status=True,laboratory_report_recieved_status=False).count()

def lab_test_released_to_herbal_care():
	return Patient_Laboratory.objects.filter(released_status=True,viewed_status=True).count()
def medical_request_to_dietary():
	return Patient_Diagosis_History.objects.filter(dietary_report_reuqest_status=True,dietary_report_recieved_status=False).count()

def notification_box():
	waiting_patients=Patient_History.objects.filter(checked_in=True,waiting_state="checked in").count()
	lab_request=Patient_Diagosis_History.objects.filter(laboratory_report_request_status=True,laboratory_report_recieved_status=False,patient_history__checked_out=False).count()
	lab_request_released=Patient_Laboratory.objects.filter(released_status=True,viewed_status=True,patient_history__checked_out=False).count()
	dietary_supplement=Patient_Diagosis_History.objects.filter(dietary_report_reuqest_status=True,dietary_report_recieved_status=False,patient_history__checked_out=False).count()
	patient_biiling_checkout=Patient_Diagosis_History.objects.filter(laboratory_report_request_status=True,laboratory_report_recieved_status=True,dietary_report_reuqest_status=True,dietary_report_recieved_status=True,patient_history__checked_out=False).count()
	print(lab_request)
	return [{'checked_in_patients':{'counts':waiting_patients,'message':'patient checked in'},'lab_request':{'counts':lab_request,'message':'lab test request sent'},'lab_request_released':{'counts':lab_request_released,'message':'lab test released'},'dietary_supplement':{'counts':dietary_supplement,'message':'patient dietary supplement requested'},'billing_checkout':{'counts':patient_biiling_checkout,'message':'have bills to settle'}}]
#,