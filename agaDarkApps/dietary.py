from django.contrib.auth.models import User,auth,Group
from django.db.models import Count ,F,Q,Sum
from .models import Patient_History,Patient_Diagosis_History,Patient_Dietary,Patient_Dietary_Details,Dietary_Dispenser_Techician,Patient_Dietary_Date_Released,Dietary_Supplementary,Dietary_Supplmentary_Details,Dietary_Supplmentary_Stock_Details
from datetime import datetime









'''
   stage 5 dietary
'''

def patient_dietary(patient_history_id,patinet_diagonsis_id,user_id,dietary_list):
	patient_dietary_history=Patient_Dietary.objects.create(patient_history=Patient_History.objects.get(pk=patient_history_id),patient_diagonsis_history_details=Patient_Diagosis_History.objects.get(pk=patinet_diagonsis_id))
	patient_dietary_history.save()
	patient_dietary_id=Patient_Dietary.objects.latest('id')
	pharmicst_who_handle_dietary=Dietary_Dispenser_Techician.objects.create(patient_dietary=Patient_Dietary.objects.get(pk=patient_dietary_id.id),techinician=User.objects.get(pk=user_id))
	pharmicst_who_handle_dietary.save()
	for dietary in range(len(dietary_list)):
		patient_dietary_list_details=Patient_Dietary_Details.objects.create(patient_dietary=Patient_Dietary.objects.get(pk=patient_dietary_id.id),dietary=Dietary_Supplementary.objects.get(pk=dietary_list[dietary]))
		patient_dietary_list_details.save()
		patient_dietary_cost_details(patient_dietary_id.id,dietary_list)
	return True


def patient_dietary_cost_details(patient_dietary_id,dietary_list):
	total_cost=0
	lists=[]
	for dietary in range(len(dietary_list)):
		dietary_cost_details=Dietary_Supplementary.objects.filter(id=dietary_list[dietary])
	
		for dietary_cost in dietary_cost_details:
			total_cost+=dietary_cost.price
	update_patient_dietary_cost=Patient_Dietary.objects.get(pk=patient_dietary_id)
	update_patient_dietary_cost.total_cost=total_cost
	update_patient_dietary_cost.save()
	return True
    	

def view_dietary_pending_list():
	return Patient_Dietary.objects.filter(patient_diagonsis_history_details__dietary_report_reuqest_status=True,patient_history__checked_in=True,patient_history__checked_out=False)
def view_patient_dietary_status(patient_history_id):
	return Patient_Dietary.objects.filter(patient_history__id=patient_history_id)
def view_patient_deietary_details(patient_history_id):
	return Patient_Dietary_Details.objects.filter(patient_dietary__patient_history__id=patient_history_id)

def input_patient_dietry_request(patient_dietary_details_id,dietary_id,dietary_dispensed_status,quantity,patient_history_id):
	get_laboratory_id=Patient_Dietary_Details.objects.filter(patient_dietary__patient_history=patient_history_id)[0]
	for items in range(len(patient_dietary_details_id)):
		input_patient_dietary_details=Patient_Dietary_Details.objects.get(pk=patient_dietary_details_id[items])
		input_patient_dietary_details.status=True
		input_patient_dietary_details.quantity=quantity[items]
		input_patient_dietary_details.price=dietary_supplement_price(dietary_id[items])
		input_patient_dietary_details.save()
		update_supplement_dieary_quanity(dietary_id[items],quantity[items])

	return True

	patient_diagnosis.save()
def dietary_supplement_price(dietary_id):
	dietary_price=Dietary_Supplementary.objects.get(pk=dietary_id)
	return dietary_price.price
def status_updates(patient_lab_id):
	patient_dietary=Patient_Dietary.objects.get(pk=patient_lab_id)
	patient_dietary.released_status=True
	patient_dietary.viewed_status=True
	#patient_diagnosis_status(patient_lab.patient_diagonsis_history_details.id)
	patient_dietary.save()
def patient_diagnosis_status(patient_diagnosis_id):
	patient_diagnosis=Patient_Diagosis_History.objects.get(pk=patient_diagnosis_id)
	patient_diagnosis.dietary_report_recieved_status=True
	#patient_diagnosis=True
	patient_diagnosis.save()
def view_dietary_history(patient_history_id):
    # return Patient_Laboratory.objects.filter(patient_history__id=patient_history_id)
    pass

def update_supplement_dieary_quanity(dietary_id,quantity):
	get_dietary_supplement=Dietary_Supplementary.objects.get(pk=dietary_id)
	get_dietary_supplement.quantity = int(get_dietary_supplement.quantity) -int(quantity)
	get_dietary_supplement.save()
	#keep dietary supplementary quantity in track
'''
dietary inventiry stock
'''

def view_dietary_list():
	return Dietary_Supplementary.objects.all()
def multiple_dietary_list(dietary_id):
	data=list()
	for items in dietary_id:
		dietary=Dietary_Supplementary.objects.get(pk=items)
		data.append({'items':dietary.dietary_name,'amount':dietary.price})
	return data

	'''
	
	for dietary in dietary_list:
		lists.append({'dietary':dietary.dietary_name,'amount':dietary.price})
	return multiple_dietary_list
	'''
def create_dietary_supplementary_cost(dietary,notes,cost,quantity_stocked,photo,user_id):
	
	if quantity_stocked > 0:
		get_dietary_name=Dietary_Supplementary.objects.filter(dietary_name=dietary)
		if not get_dietary_name.exists():
			create_dietary_list=Dietary_Supplementary.objects.create(dietary_name=dietary,notes=notes,price=cost,photo=photo,quantity=quantity_stocked)
			create_dietary_list.save()
			dietary_id=Dietary_Supplementary.objects.latest('id')
			diet_supplement=check_dietary_supplement_stocking_info(dietary_id.id,quantity_stocked,cost,user_id)
			return diet_supplement

		else:
			return "dietary record already exist"
		#	check_dietary_supplement_stocking_info(dietary_id,quantity_stocked,cost,user_id)
	else:
		return "quantity is zero"
def edit_dietary_list_details(dietary,notes,cost,dietary_id):
	get_dietary_details=Dietary_Supplementary.objects.get(pk=dietary_id)
	get_dietary_details.dietary=dietary
	get_dietary_details.notes=notes
	get_dietary_details.save()
	return True

def dietary_supplement_stocking():
	return Dietary_Supplmentary_Details.objects.all()
def dietary_supplement_stocking_details_history(dietary_id):
	return Dietary_Supplmentary_Stock_Details.objects.filter(dietary_details__dietary__id=dietary_id)
def check_dietary_supplement_stocking_info(dietary_id,quantity_stocked,cost,user_id):
	dietary_stock_details=create_dietary_supplement_stocking_details(dietary_id,quantity_stocked,cost,user_id)
	return dietary_stock_details

		
def create_dietary_supplement_stocking_details(dietary_id,quantity_stocked,cost,user_id):
	if quantity_stocked > 0:
		stocking_dietary=Dietary_Supplmentary_Details.objects.create(dietary=Dietary_Supplementary.objects.get(pk=dietary_id),quantity=quantity_stocked,quantity_stocked=quantity_stocked,status=True)
		stocking_dietary.save()
		stocking_dietary_id=Dietary_Supplmentary_Details.objects.latest('id')
		dietary_history=dietary_stocking_tracking_history(stocking_dietary_id.id,quantity_stocked,quantity_stocked,cost,cost,quantity_stocked,user_id)
		return dietary_history
	else:
		return False

def update_dietary_supplement_stocking_details(dietary_id,quantity_stocked,cost):
	if quantity_stocked > 0:
		get_stock_details=Dietary_Supplmentary_Details.objects.get(dietary__id=dietary_id)
		get_stock_details.quantity=int(get_stock_details.quantity+quantity_stocked)
		get_stock_details.quantity_stocked=quantity_stocked
		get_stock_details.save()
		return True
	else:
		return False

def dietary_stocking_tracking_history(Dietary_Supplmentary_id,new_quantity,old_quantity,old_price,new_price,old_stocked_quantity,user_id):
	#print('hello world',Dietary_Supplmentary_id)
	create_stock_history=Dietary_Supplmentary_Stock_Details.objects.create(dietary_details=Dietary_Supplmentary_Details.objects.get(pk=Dietary_Supplmentary_id),new_quantity=new_quantity,old_quantity=old_quantity,dietary_recent_cost=new_price,dietary_old_cost=old_price,quantity_at_time_of_stocking=old_stocked_quantity,stocked_by=User.objects.get(pk=user_id))
	create_stock_history.save()
	return True

def update_dietary_details(dietary_id,dietary,notes):
	get_dietary_updates=Dietary_Supplementary.objects.get(pk=dietary_id)
	get_dietary_updates.dietary_name=dietary
	get_dietary_updates.notes=notes
	get_dietary_updates.save()
	return True

def dietary_need_restock():
	return Dietary_Supplmentary_Stock_Details.objects.filter(dietary_details__dietary__quantity__lte=10)
def deitary_stock_info(dietary_id):
	return  Dietary_Supplmentary_Stock_Details.objects.filter(dietary_details__dietary__id=dietary_id).order_by('-id')[0]

def update_dietary_details_stock(dietary_id,quantity,price,user_id):
	get_dietary=Dietary_Supplementary.objects.get(pk=dietary_id)
	quantity_stock_history=Dietary_Supplmentary_Details.objects.filter(dietary__id=dietary_id).order_by('-id')[0]
	print('tested ',quantity_stock_history.quantity_stocked)
	print(type(get_dietary.quantity), type(quantity))
	total_quantity_stocked=int(get_dietary.quantity)+int(quantity)
	old_quantity_stocked=quantity_stock_history.quantity_stocked
	quantity_at_time_of_stocking=get_dietary.quantity
	stocking_history=update_dietary_stock_quantity_history(dietary_id,total_quantity_stocked,quantity,old_quantity_stocked,quantity_at_time_of_stocking,price,get_dietary.price,user_id)
	if stocking_history == True:
		price_quantity_update=update_dietary_cost_price(dietary_id,quantity,price)
		return price_quantity_update
	else:
	 	return False


def update_dietary_cost_price(dietary_id,quantity,cost):
	dietary=Dietary_Supplementary.objects.get(pk=dietary_id)
	dietary.price=cost
	dietary.quantity+=int(quantity)
	dietary.save()
	return True

def update_dietary_stock_quantity_history(dietary_id,total_quantity_stock,new_quantity,old_quantity,quantity_at_time_of_stocking,new_price,old_price,user_id):
	if int(new_quantity) > 0:
		stocking_dietary=Dietary_Supplmentary_Details.objects.create(dietary=Dietary_Supplementary.objects.get(pk=dietary_id),quantity=total_quantity_stock,quantity_stocked=new_quantity,status=True)
		stocking_dietary.save()
		stocking_dietary_id=Dietary_Supplmentary_Details.objects.latest('id')
		#get last stock

		stocking_history=dietary_stocking_tracking_history(stocking_dietary_id.id,new_quantity,old_quantity,old_price,new_price,quantity_at_time_of_stocking,user_id)
		if stocking_history == True:
			return True
		else:
			return False


def  patient_dietary_search(searchs,hospital_id):
	return Patient_Dietary.objects.values('patient_history__patient__First_Name','patient_history__patient__Last_Name','patient_history__patient__Date_Of_Birth','patient_history__patient__Telephone','patient_history__patient__card_number','patient_history__id').filter(Q(patient_history__patient__First_Name=searchs)|Q(patient_history__patient__Last_Name=searchs)|Q(patient_history__patient__Telephone=searchs),patient_history__hospital__id=hospital_id).annotate(total_visit=Count('patient_history__patient__id')).order_by()
 

  

