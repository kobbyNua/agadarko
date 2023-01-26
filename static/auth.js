$(document).ready(function(){

	   $('#login_user').submit(function(e){
	   	   e.preventDefault()
	   	    $.ajax({


      	         url:'/auth',
      	         data:$(this).serialize(),
      	         type:'post',
      	         dataType:'json',
      	         beforeSend:function(){
      	    	       $('#login_user .msg-box').html('ascending request')
      	         },
      	         success:function(data){
                        console.log(data)
      	         	if(data.status === "success"){
      	          	      $('#login_user .msg-box').html(data.success)
      	          	      window.location="/dashboard"
      	          	}

      	          	else if(data.status === "error"){
      	          		$('#login_user .msg-box').html(data.error)

      	          	}

      	        },
      	        error:function(){
      	        	$('#login_user .msg-box').html('network timeout')
      	        }



            })
	   })
})