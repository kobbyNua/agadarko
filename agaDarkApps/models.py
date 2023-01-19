from django.db import models
from datetime import date,datetime
from django.contrib.auth.models import User

# Create your models here.


class Books(models.Model):
	name=models.CharField(max_length=150)
	authors=models.CharField(max_length=150)
	date_published=models.DateField()
'''
 * hospital regional location is stage 1
 * stage 2 entails user, group, role


'''
'''
class Group(models.Model):
	name=models.CharField(max_length=150)
class Permissions(models.Model):
	name=models.CharField(max_length=150)
	context=models.CharField(max_length=150)
class Group_Persmission(models.Model):
	group=models.ForeignKey(Group,on_delete=models.CASCADE)
	permission=models.ForeignKey(Permissions,on_delete=models.CASCADE)
class Staff_Group_Permission(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      group=models.ForeignKey(Group,on_delete=models.CASCADE)
      permission=models.ForeignKey(Permissions,on_delete=models.CASCADE)
'''		
class Region(models.Model):
	region=models.CharField(max_length=150)
class Hospital(models.Model):
      name=models.CharField(max_length=150)
      adminstrator=models.ForeignKey(User,on_delete=models.CASCADE)
      telephone=models.CharField(max_length=150)
      email=models.EmailField(max_length=255,default="info@example.com")
      Town=models.CharField(max_length=150)
      region=models.ForeignKey(Region,on_delete=models.CASCADE)
class Hospital_Staff(models.Model):
	staff=models.ForeignKey(User,on_delete=models.CASCADE)
	telephone=models.CharField(max_length=170,default=" ")
	hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)
'''
class Branch(models.Model):
      branch=models.CharField(max_length=150)
      branch_code=models.CharField(max_length=150)
      telephone=models.CharField(max_length=150)
      town=models.CharField(max_length=150)
      region=models.ForeignKey(Region,on_delete=models.CASCADE)
      adminstrator=models.CharField(max_length=150)
'''
'''
    * stage 3 patient opd recods
'''
class Patient(models.Model):
		First_Name=models.CharField(max_length=150)
		Last_Name=models.CharField(max_length=150)
		Date_Of_Birth=models.DateField()
		Telephone=models.CharField(max_length=150)
		region=models.ForeignKey(Region,on_delete=models.CASCADE)
		Town=models.CharField(max_length=150)
		card_number=models.CharField(max_length=150,default="")
		unit_no=models.CharField(max_length=150,default="")
		registration_number=models.CharField(max_length=150)
		registered_by=models.ForeignKey(User,on_delete=models.CASCADE)
		date_registered=models.DateField()
		'''
		def save(self,*args,**kwargs):
			self.date_registered="{}-{}-{} {}:{}:{} {}".format(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().strftime("%I"),datetime.now().strftime("%M"),datetime.now().strftime("%S"),datetime.now().strftime("%p"))
        '''
'''
   search patient by name or date of birth or telephone
   check in patient and check out patient when done
   do n't check out patient if hospital if the patient will come for review
'''
class Patient_History(models.Model):
	patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
	hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)
	nurse=models.ForeignKey(User,on_delete=models.CASCADE)
	date_reported=models.DateField()
	attended_to=models.BooleanField(default=True)
	checked_in=models.BooleanField(default=False)
	checked_out=models.BooleanField(default=False)
	waiting_state=models.CharField(max_length=150,default="waiting")
	checked_in_date_time=models.DateField(default="1982-01-02")
	checked_out_date_time=models.DateField(default="1982-01-02")
	'''
	   def save(self,*args,**kwargs):
	   	
	   	
	   	#self.date_reported="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().strftime("%I"),datetime.now().strftime("%M"),datetime.now().strftime("%S"))
	   	if self.checked_in == True:
	   		self.checked_in_date_time="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
	   	elif self.checked_out == True:
	   		self.checked_out_date_time ="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
        
    '''
'''
   * Stage 4 Colour 
'''       
class OPD_Vitals(models.Model):
       vital_type=models.CharField(max_length=150)

'''

patient history opd vital must be taken by the doctor
'''
class Patient_History_OPD_Vitals_Details(models.Model):
       patient_history=models.ForeignKey(Patient_History,on_delete=models.CASCADE)
       vitals=models.ForeignKey(OPD_Vitals,on_delete=models.CASCADE)
       details=models.CharField(max_length=150)

'''
class Patient_History_OPD_Vitals_History(models.Model):
	 patient_opd_history=models.ForeignKey(Patient_History,on_delete=models.CASCADE)
	 patient_complaint=models.TextField()
'''
class Patient_Diagosis_History(models.Model):
		patient_history=models.ForeignKey(Patient_History,on_delete=models.CASCADE)
		patient_complaint=models.TextField()
		doctor_dignosis_report=models.TextField(default="")
		doctor=models.ForeignKey(User,on_delete=models.CASCADE)
		laboratory_report_request_status=models.BooleanField(default=False)
		laboratory_report_recieved_status=models.BooleanField(default=False)
		dietary_report_reuqest_status=models.BooleanField(default=False)
		dietary_report_recieved_status=models.BooleanField(default=False)
		date_diagosed=models.DateField()
		'''
		def save(self,*args,**kwargs):
			self.date_diagosed="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
		'''
'''
 Stage 5 laborary
'''
'''
class Referrals(models.Model):
	referral_type=models.CharField(max_length)
class Patient_Referrals(models.Model):
	patient_history=models.ForeignKey(Patient_History,on_delete=models.CASCADE)
	referrals=models.ForeignKey(Patient_History,on_delete=models.CASCADE)
	referral_status=models.BooleanField(default=False)
	date_referred=models.DateTimeField()
	def save(self,*args,**kwargs):
		self.date_referred="{}-{}-{} {}:{}:{} {}".format(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().strftime("%I"),datetime.now().strftime("%M"),datetime.now().strftime("%S"),datetime.now().strftime("%p"))
'''
class Lab_Test_Cost_Details(models.Model):
	test_type=models.CharField(max_length=150)
	notes=models.TextField()
	cost=models.FloatField(max_length=150,default=0.00)
	  
class Patient_Laboratory(models.Model):
	patient_history=models.ForeignKey(Patient_History,on_delete=models.CASCADE)
	patient_diagonsis_history_details=models.ForeignKey(Patient_Diagosis_History,on_delete=models.CASCADE)  
	date_reported=models.DateField()
	lab_report_status_seen=models.BooleanField(default=False)

	released_status=models.BooleanField(default=False)
	viewed_status=models.BooleanField(default=False)
	total_cost=models.FloatField(max_length=150,default=0.00)

class Patient_Laboratory_Details(models.Model):
         patient_laboratory=models.ForeignKey(Patient_Laboratory,on_delete=models.CASCADE)
         lab_test_type=models.ForeignKey(Lab_Test_Cost_Details,on_delete=models.CASCADE)
         lab_test_status_report=models.CharField(max_length=150,default="")

class laboratory_test_techician(models.Model):
	patient_laboratory=models.ForeignKey(Patient_Laboratory,on_delete=models.CASCADE)
	techinician=models.ForeignKey(User,on_delete=models.CASCADE)
class Patient_Laboratory_Date_Released(models.Model):
	patient_laboratory=models.ForeignKey(Patient_Laboratory,on_delete=models.CASCADE)
	date_released=models.DateTimeField(default=date.today)

'''
  Stage 6 medication/dietary/pharmacy
'''
class Patient_Dietary(models.Model):
		patient_history=models.ForeignKey(Patient_History,on_delete=models.CASCADE)
		patient_diagonsis_history_details=models.ForeignKey(Patient_Diagosis_History,on_delete=models.CASCADE)
		date_reported=models.DateTimeField()
		viewed_status=models.BooleanField(default=False)
		released_status=models.BooleanField(default=False)
		total_cost=models.FloatField(default=0.00)
		def save(self,*args,**kwargs):
			self.date_reported="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
			super().save(*args,**kwargs)

class Dietary_Supplementary(models.Model):
	dietary_name=models.CharField(max_length=150)
	notes=models.TextField()
	price=models.FloatField(default=0.00)
	photo=models.FileField(upload_to="uploads",default=" ")
	quantity=models.IntegerField(default=10)

class Patient_Dietary_Details(models.Model):
	patient_dietary=models.ForeignKey(Patient_Dietary,on_delete=models.CASCADE)
	dietary=models.ForeignKey(Dietary_Supplementary,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=0)
	price=models.FloatField(default=0.00)
	status=models.BooleanField(default=False)

class Dietary_Dispenser_Techician(models.Model):
	patient_dietary=models.ForeignKey(Patient_Dietary,on_delete=models.CASCADE)
	techinician=models.ForeignKey(User,on_delete=models.CASCADE)

class Patient_Dietary_Date_Released(models.Model):
	patient_dietary=models.ForeignKey(Patient_Dietary,on_delete=models.CASCADE)
	dispensed_released=models.DateTimeField(default=date.today)



class Dietary_Supplmentary_Details(models.Model):
	dietary=models.ForeignKey(Dietary_Supplementary,on_delete=models.CASCADE)
	quantity=models.IntegerField(default=0)
	quantity_stocked=models.IntegerField(default=0)
	status=models.BooleanField(default=False)
	date_stocked=models.DateTimeField()
	def save(self,*args,**kwargs):
		self.date_stocked="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
		super().save(*args,**kwargs)
	    #quantity field represent the total quanity stocked (which is the quantity remaining + the quantity stocked)
	    #quantity stocked is the new quantity stocked
class Dietary_Supplmentary_Stock_Details(models.Model):
	dietary_details=models.ForeignKey(Dietary_Supplmentary_Details,on_delete=models.CASCADE)
	dated_stocked=models.DateTimeField()
	new_quantity=models.IntegerField()
	old_quantity=models.IntegerField()
	dietary_recent_cost=models.FloatField(default=0.00)
	dietary_old_cost=models.FloatField(default=0.00)
	quantity_at_time_of_stocking=models.IntegerField()
	stocked_by=models.ForeignKey(User,on_delete=models.CASCADE)
	def save(self,*args,**kwargs):
		self.dated_stocked="{}-{}-{}".format(datetime.now().year,datetime.now().month,datetime.now().day)
		super().save(*args,**kwargs)
	

'''
class Patient_Bills_Record(model.Models):
	  pass
class Inventory_Stock(model.Models):
	  pass
'''