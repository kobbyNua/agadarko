'''
from rest_framework import serializers
from .models import Books,Region,Hospital,Hospital_Staff,Patient,Patient_History



class BooksSerializers(serializers.ModelSerializer):
 	    class Meta:
 	          model = Books
 	          fields ="__all__"

class RegionSerializers(serializers.ModelSerializer):
	    class Meta:
	    	  model = Region
	    	  fields = ['region']

class HospitalSerializers(serializers.ModelSerializer):
	    class Meta:
	    	   model = Hospital
	    	   fields = ['name','adminstrator','telephone','Town','region']

class HospitalStaffSerializers(serializers.ModelSerializer):
	    class Meta:
	    	    model=Hospital_Staff
	    	    fields = ['staff','hospital']
'''