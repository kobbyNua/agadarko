from django.urls import path
from . import views

urlpatterns=[
   path('dashboard/',views.dashboard,name='dashboard'),
   path('patient-opd-panel',views.patient_opd_panel,name='patient_opd_panel'),
   path('patient-search',views.patient_searchs,name="patient_searchs"),
   path('view-patient-detail/<str:patient_card_id>',views.view_patient_detail,name="view_patient_detail"),
   path('create-patient',views.create_patient,name="create-patient"),
   path('view-opd-vitals/',views.view_opd_vitals,name="view_opd_vitals"),
   path('create-opd-vital/',views.create_opd_vital,name="create_opd_vital"),
   path('edit-opd-details/',views.edit_opd_details,name="edit_opd_details"),
   path('waiting-patient-list',views.waiting_patient_list,name="waiting_patient_list"),
   path('patient-profile/<int:patient_history_id>',views.patient_profile,name="patient_profile"),
   path('create-patient-opd-vitals',views.create_patient_opd_vitals,name="create_patient_opd_vitals"),
   path('create-patient-complaints-diagonsis',views.create_patient_complaints_diagonsis,name="create_patient_complaints_diagonsis"),
   path('edit-doctor-diagonsis',views.edit_doctor_diagonsis,name="edit_doctor_diagonsis"),
   path('create-patient-lab-request',views.create_patient_lab_request,name="create_patient_lab_request"),
   path('patient-medical-history-records',views.patient_medical_history_records,name="patient_medical_history_records"),
  
   path('create-inventary-dietary-stock',views.create_inventary_dietary_stock,name="create_inventary_dietary_stock"),
   path('create-patient-dietary-request',views.create_patient_dietary_request,name="create_patient_dietary_request"),
   path('view-patient-dietary-lists',views.view_patient_dietary_lists,name="view_patient_dietary_lists"),
   path('view-patient-dietary-details/<int:patient_history_id>/',views.view_patient_dietary_details,name="view_patient_dietary_details"),
   path('dispen-patient-dietary',views.dispen_patient_dietary,name="dispen_patient_dietary"),

   path('view-lab-test-types',views.view_lab_test_types,name='view_lab_test_types'),
   path('create-lab-test-types',views.create_lab_test_types,name="create_lab_test_types"),
   path('edit-lab-test-type',views.edit_lab_test_type,name="edit_lab_test_type"),
   path('view-lab-tests-request',views.view_lab_tests_request,name='view_lab_tests_request'),
   path('view-patient-required-lab-test/<int:patient_history_id>',views.view_patient_required_lab_test,name='view_patient_required_lab_test'),
   path('input-lab-test-result-details',views.input_lab_test_result_details,name="input lab test result"),

   path('staff-management/',views.staff_management,name='staff_management'),
   path('staff-user-management/<str:staff_id>',views.staff_user_management,name='staff_user_management'),
   path('user-management/',views.user_management,name='user_management'),
   path('laboratory-management/',views.laboratory_management,name='user_management'),
   path('laboratory-test-details/<str:lab_test_id>',views.laboratory_test_management_details,name='user_management'),

   path('dietary-stocking/',views.dietary_stocking,name="dietary_stocking"),
   path('dietary-stocking-view/<str:dietary_id>',views.dietary_stocking_view,name='dietary_stocking_view'),
   path('update-dietary-inventary-stock',views.update_dietary_inventary_stock,name="update_dietary_inventary_stock"),
   path('update-dietary-supplement-details',views.update_dietary_supplement_details,name="update_dietary_supplement_details"),
   path('company/',views.company,name="company"),
   path('set-hospital-details',views.set_hospital_details,name="set_hospital_details"),
   path('create-staff-details',views.create_staff_details,name='create_staff_details'),
   path('staff-update',views.staff_update,name='update_staff'),
   path('change-password',views.change_pass,name="change password")
   #path("",views.home,name="home"),
   #path("books-list/",views.booksList,name="bookList"),
   #path('book-details/<int:id>',views.bookDetails,name="book-details"),
   #path("create-books-details/",views.createBooksDetails,name="create-books-details"),
   #path('update-book-details/<int:id>',views.updateBookDetails,name="update-book-details"),


]