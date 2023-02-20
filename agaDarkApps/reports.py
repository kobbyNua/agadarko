from .models import OPD_Charges,OPD_Payment_Charges,Medical_History_Diagnosis_Payment
from django.db.models import Count ,F,Q,Sum,Value
from dateutil.relativedelta import *
from datetime import *


def daily_payment_charges():
    return Medical_History_Diagnosis_Payment.objects.filter(date_paid=date.today()).aggregate(total_payments=Sum('amount_paid'),total_patients=Count('patient_history__id'))
def daily_opd_charge_payment():
    return OPD_Payment_Charges.objects.filter(date_paid=date.today()).aggregate(total_payments=Sum('amount_paid'),total_patients=Count('patient_history__id'))
def opdChargesReports(start_date,end_date):
    return OPD_Payment_Charges.objects.filter(date_paid__gte=start_date,date_paid__lte=end_date).aggregate(total_amout_paid=Sum('amount_paid'),total_patients=Count('patient_history__id'))

def generate_medical_diagnosis_paymem_record(start_date,end_date):
    return Medical_History_Diagnosis_Payment.objects.filter(date_paid__gte=start_date,date_paid__lte=end_date).aggregate(total_amout_paid=Sum('amount_paid'),total_patients=Count('patient_history__id'))

def receivers_balance_sheet():
    pass

