


$(document).ready(function(){
       //create company details
	  $('#company').submit(function(e){
             $('#responseBox').modal('show')
             submitForms(this,'/set-hospital-details')
 
             e.preventDefault()

	  })

        //create hospital staff account
	  $('#createStaff').submit(function(e){
	
             $('#responseBox').modal('show')
             submitForms(this,'/create-staff-details')
             e.preventDefault()
 
	  })
        //update hospital staff account
        $("#updateStaff").submit(function(e){
              $('#responseBox').modal('show')
              submitForms(this,'/staff-update')
              e.preventDefault()
        })

        //change password

        $('#change_password').submit(function(e){
            $('#responseBox').modal('show')
            submitForms(this,'/change-password')
            e.preventDefault()
        })
        //laboratory test details
        $('#laboratory').submit(function(e){
            $('#responseBox').modal('show')
            submitForms(this,'/create-lab-test-types')            
            e.preventDefault()
        })

        //edit laboratory test
        $('#edit_lab_test').submit(function(e){
            $('#responseBox').modal('show')
            submitForms(this,'/edit-lab-test-type')  
            e.preventDefault()
        })
   $("#createDietarySupplement").submit(function(e){

            $('#responseBox').modal('show')
            e.preventDefault()
            formFileUpload(this,'/create-inventary-dietary-stock')
           
           
   })

   $('#update_dietary_stock').submit(function(e){
         $('#responseBox').modal('show')
         e.preventDefault()
         submitForms(this,'/update-dietary-inventary-stock')

   })

   $('#updateDieataryDetails').submit(function(e){
         $('#responseBox').modal('show')
         e.preventDefault()
         submitForms(this,'/update-dietary-supplement-details')

   })  
   $('#patient_search input[name=search]').keyup(function(e){
        e.preventDefault()
        serverData($('#patient_search'),'/patient-search')

   }) 
   $('#patientRegistration').submit(function(e){
        $('#responseBox').modal('show')
        e.preventDefault()
        submitForms(this,'/create-patient')
   })

   $('#create_opd_details').submit(function(e){
      e.preventDefault()
      $('#responseBox').modal('show')
      submitForms(this,"/create-patient-opd-vitals")
  })

  $('#patient_complaints_details').submit(function(e){
      e.preventDefault()
      $('#responseBox').modal('show')
      submitForms(this,"/create-patient-complaints-diagonsis")
  })  

  $('#doctor_diagnosis_report').submit(function(e){
      e.preventDefault()
      $('#responseBox').modal('show')
      submitForms(this,"/edit-doctor-diagonsis")
  }) 
//request for patient laboratory by medical doctor
  $('#select_lab_test').submit(function(e){
      e.preventDefault()
      $('#responseBox').modal('show')
      submitForms(this,"/create-patient-lab-request")
  }) 
  //lab test results entry

   $("#lab_results_entery").submit(function(e){
         e.preventDefault()
         $('#responseBox').modal('show')
         submitForms(this,"/input-lab-test-result-details")
   })
//Dietary request
   $("#select_dietary_supplement").submit(function(e){
      e.preventDefault()
      $('#responseBox').modal('show')
      submitForms(this,"/create-patient-dietary-request")
  })
  //dispens dietary
   $('#dispense_dietary').submit(function(e){
        e.preventDefault()
        $('#responseBox').modal('show')
        submitForms(this,'/dispen-patient-dietary')
   })

   $('#select_lab_test select[name=lab_test]').change(function(e){
        e.preventDefault()
        onselectChange(this,'#selected_lab_test tbody','/multiple-lab-test_list')
       
   })
   $('#select_dietary_supplement select[name=dietary]').change(function(e){
      e.preventDefault()
      onselectChange(this,'#selected_dietary_supplement tbody','/multiple-dietary-supplement-list')
     
    })
     
    $('#search_patient_medical_history input[name=]').keyup(function(e){
         
      
      e.preventDefault()
      serverData_1(this,'/patient-medical-history-search')
    })
  
})

/*$(document).ready(function(){


         $("#createDietarySupplement").submit(function(e){
                    e.preventDefault()
                  formdata=new FormData(this)
                    $('#responseBox').modal('show')
                   $.ajax({
                    url:'/create-inventary-dietary-stock',
                    data:formdata,
                    type:'post',
                    dataType:'json',
                    cache:false,
                    contentType:false,
                    processData:false,

                     beforSend:function(){
                         $('#responseBox .modal-body .msg-box').html('ascending request')
                     },
                     success:function(data){
                        if(data.status === "success"){
                              $('#responseBox .modal-body .msg-box').html(data.success)
                              window.location=""
                        }

                        else if(data.status === "error"){
                              $('#responseBox .modal-body .msg-box').html(data.error)

                        }

                    },
                    error:function(){
                        $('#responseBox .modal-body .msg-box').html('network timeout')
                    }


                  });

              


         })

})*/
submitForms=(form_id,urls)=>{

            $.ajax({


      	         url:urls,
      	         data:$(form_id).serialize(),
      	         type:'post',
      	         dataType:'json',
      	         beforeSend:function(){
      	    	       $('#responseBox .modal-body .msg-box').html('ascending request')
      	         },
      	         success:function(data){
                        console.log(data)
      	         	if(data.status === "success"){
      	          	      $('#responseBox .modal-body .msg-box').html(data.success)
      	          	      //window.location=""
      	          	}

      	          	else if(data.status === "error"){
      	          		$('#responseBox .modal-body .msg-box').html(data.error)

      	          	}

      	        },
      	        error:function(){
      	        	$('#responseBox .modal-body .msg-box').html('network timeout')
      	        }



            })
}

formFileUpload=(form_id,urls)=>{
                  formdata=new FormData(form_id)

       $.ajax({
                    url:urls,
                    data:formdata,
                    type:'post',
                    dataType:'json',
                    cache:false,
                    contentType:false,
                    processData:false,

                     beforSend:function(){
                         $('#responseBox .modal-body .msg-box').html('ascending request')
                     },
                     success:function(data){
                        if(data.status === "success"){
                              $('#responseBox .modal-body .msg-box').html(data.success)
                              window.location=""
                        }

                        else if(data.status === "error"){
                              $('#responseBox .modal-body .msg-box').html(data.error)

                        }

                    },
                    error:function(){
                        $('#responseBox .modal-body .msg-box').html('network timeout')
                    }


       });



}
serverData=(form_id,urls)=>{



      $.ajax({
             url:urls,
             data:form_id.serialize(),
             type:'post',
             dataType:'json',
             beforeSend:function(){
                  rows=""
                  rows+='<tr><td colspan="5" align="center">wait. search for result may take few seconds</td></tr>'
                  $("#search_results").html(rows)
             },
             success:function(data){
                  rows=""
                  console.log(data)
                  if (data.result.length == ""){
                    rows+='<tr><td colspan="5" align="center">no results found</td></tr>'
                    //$("#search_results").html(rows)
                        //$("#search_results").html('<tr><td>no results found</td></tr>')
                  }
                  else{
                      for(index=0;index<data.result.length;index++){
                        rows+="<tr>"
                        rows+='<td>'+data.result[index].fullname+'</td>'
                        rows+='<td>'+data.result[index].telephone+'</td>'
                        rows+='<td>'+data.result[index].dob+'</td>'
                         //rows+='<td>'+data.result[index].card+'</td>'
                        rows+='<td>'+data.result[index].total_visit+'</td>'
                        rows+='<td><a href="/view-patient-detail/'+data.result[index].patient_id+'" class="btn btn-info">view and check-in</a></td>'
                        rows+='</tr>'
                        console.log(rows)
                      }
                }
                  $("#search_results").html(rows)
                


             },
             error:function(){
                  console.log('network timeout')
             }
      })


}
serverData_1=(form_id,urls)=>{



      $.ajax({
             url:urls,
             data:form_id.serialize(),
             type:'post',
             dataType:'json',
             beforeSend:function(){
                  rows=""
                  rows+='<tr><td colspan="5" align="center">wait. search for result may take few seconds</td></tr>'
                  $("#search_results").html(rows)
             },
             success:function(data){
                  rows=""
                  console.log(data)
                  if (data.result.length == ""){
                    rows+='<tr><td colspan="5" align="center">no results found</td></tr>'
                    //$("#search_results").html(rows)
                        //$("#search_results").html('<tr><td>no results found</td></tr>')
                  }
                  else{
                      for(index=0;index<data.result.length;index++){
                        rows+="<tr>"
                        rows+='<td>'+data.result[index].fullname+'</td>'
                        rows+='<td>'+data.result[index].telephone+'</td>'
                        rows+='<td>'+data.result[index].dob+'</td>'
                         //rows+='<td>'+data.result[index].card+'</td>'
                        rows+='<td>'+data.result[index].total_visit+'</td>'
                        rows+='<td><a href="/view-patient-detail/'+data.result[index].patient_id+'" class="btn btn-info">view and check-in</a></td>'
                        rows+='</tr>'
                        console.log(rows)
                      }
                }
                  $("#search_results").html(rows)
                


             },
             error:function(){
                  console.log('network timeout')
             }
      })


}
getInfo=(id,url)=>{

      $.ajax({


      	     url:'',
      	     data:{id:id},
      	     type:'get',
      	     dataType:'json',
      	     success:function(data){
      	     	  console.log(data)
      	     },
      	     error:function(){
      	     	  console.log('network timeout')
      	     }
      })

}

onselectChange=(selector_id,results,url)=>{
      options=$(selector_id).val()

      $.ajax({


            url:url,
            data:{choose:JSON.stringify(options)},
            type:'get',
            dataType:'json',
            success:function(data){
                  row=""
                  console.log(data)
                  total=0
                  for(var index=0;index<data.status.length;index++){
                        row+="<tr>"
                        row+="<td>"+data.status[index].items+"</td>"
                        row+="<td>GHS "+data.status[index].amount+"</td>"
                        row+="</tr>"
                        total+=data.status[index].amount
                        
                  }
                  row+='<tr><td>Total </td><td>GHS '+total+'</td></tr>'
                  
                  //console.log(results)
                  $(results).html(row)
            },
            error:function(){
                    console.log('network timeout')
            }
      })    

}


  

