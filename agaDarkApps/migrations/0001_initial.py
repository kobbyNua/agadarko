# Generated by Django 3.2.4 on 2023-01-24 14:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('authors', models.CharField(max_length=150)),
                ('date_published', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Dietary_Supplementary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dietary_name', models.CharField(max_length=150)),
                ('notes', models.TextField()),
                ('price', models.FloatField(default=0.0)),
                ('photo', models.FileField(default=' ', upload_to='uploads')),
                ('quantity', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dietary_Supplmentary_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('quantity_stocked', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('date_stocked', models.DateTimeField()),
                ('dietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.dietary_supplementary')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('telephone', models.CharField(max_length=150)),
                ('email', models.EmailField(default='info@example.com', max_length=255)),
                ('Town', models.CharField(max_length=150)),
                ('adminstrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lab_Test_Cost_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(max_length=150)),
                ('notes', models.TextField()),
                ('cost', models.FloatField(default=0.0, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='OPD_Charges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_time_charge', models.FloatField(default=0.0)),
                ('second_time_charge', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='OPD_Vitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vital_type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=150)),
                ('Last_Name', models.CharField(max_length=150)),
                ('Date_Of_Birth', models.DateField()),
                ('Telephone', models.CharField(max_length=150)),
                ('Town', models.CharField(max_length=150)),
                ('card_number', models.CharField(default='', max_length=150)),
                ('unit_no', models.CharField(default='', max_length=150)),
                ('registration_number', models.CharField(default='', max_length=150)),
                ('waiting_state', models.CharField(default='checked out', max_length=120)),
                ('date_registered', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Diagosis_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_complaint', models.TextField()),
                ('doctor_dignosis_report', models.TextField(default='')),
                ('laboratory_report_request_status', models.BooleanField(default=False)),
                ('laboratory_report_recieved_status', models.BooleanField(default=False)),
                ('dietary_report_reuqest_status', models.BooleanField(default=False)),
                ('dietary_report_recieved_status', models.BooleanField(default=False)),
                ('date_diagosed', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Dietary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reported', models.DateTimeField()),
                ('viewed_status', models.BooleanField(default=False)),
                ('released_status', models.BooleanField(default=False)),
                ('total_cost', models.FloatField(default=0.0)),
                ('patient_diagonsis_history_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_diagosis_history')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reported', models.DateField()),
                ('case_number', models.CharField(default='', max_length=120)),
                ('attended_to', models.BooleanField(default=True)),
                ('checked_in', models.BooleanField(default=False)),
                ('checked_out', models.BooleanField(default=False)),
                ('waiting_state', models.CharField(default='pending', max_length=150)),
                ('checked_in_date_time', models.DateField()),
                ('checked_out_date_time', models.DateField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.hospital')),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reported', models.DateField()),
                ('lab_report_status_seen', models.BooleanField(default=False)),
                ('released_status', models.BooleanField(default=False)),
                ('viewed_status', models.BooleanField(default=False)),
                ('total_cost', models.FloatField(default=0.0, max_length=150)),
                ('patient_diagonsis_history_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_diagosis_history')),
                ('patient_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_history')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Laboratory_Dietary_Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_total_cost', models.FloatField(default=0.0)),
                ('supplement_total_cost', models.FloatField(default=0.0)),
                ('total_cost', models.FloatField(default=0.0)),
                ('patient_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_history')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Laboratory_Dietary_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.FloatField(default=0.0)),
                ('receipts', models.CharField(max_length=120)),
                ('date_paid', models.DateField()),
                ('lab_supplement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_laboratory_dietary_cost')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Laboratory_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_test_status_report', models.CharField(default='', max_length=150)),
                ('lab_test_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.lab_test_cost_details')),
                ('patient_laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_laboratory')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Laboratory_Date_Released',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_released', models.DateTimeField(default=datetime.date.today)),
                ('patient_laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_laboratory')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_History_OPD_Vitals_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=150)),
                ('patient_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_history')),
                ('vitals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.opd_vitals')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Dietary_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('status', models.BooleanField(default=False)),
                ('dietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.dietary_supplementary')),
                ('patient_dietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_dietary')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Dietary_Date_Released',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispensed_released', models.DateTimeField(default=datetime.date.today)),
                ('patient_dietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_dietary')),
            ],
        ),
        migrations.AddField(
            model_name='patient_dietary',
            name='patient_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_history'),
        ),
        migrations.AddField(
            model_name='patient_diagosis_history',
            name='patient_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_history'),
        ),
        migrations.AddField(
            model_name='patient',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.region'),
        ),
        migrations.AddField(
            model_name='patient',
            name='registered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OPD_Payment_Charges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.FloatField(default=0.0)),
                ('recepit', models.CharField(default='', max_length=120)),
                ('date_paid', models.DateField()),
                ('patient_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_history')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OPD_Charges_Updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_time_old_charge', models.FloatField(default=0.0)),
                ('second_time_old_charge', models.FloatField(default=0.0)),
                ('date_edited', models.DateField()),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='laboratory_test_techician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_laboratory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_laboratory')),
                ('techinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(default=' ', max_length=170)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.hospital')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.region'),
        ),
        migrations.CreateModel(
            name='Dietary_Supplmentary_Stock_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dated_stocked', models.DateTimeField()),
                ('new_quantity', models.IntegerField()),
                ('old_quantity', models.IntegerField()),
                ('dietary_recent_cost', models.FloatField(default=0.0)),
                ('dietary_old_cost', models.FloatField(default=0.0)),
                ('quantity_at_time_of_stocking', models.IntegerField()),
                ('dietary_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.dietary_supplmentary_details')),
                ('stocked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dietary_Dispenser_Techician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_dietary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agaDarkApps.patient_dietary')),
                ('techinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
