$(document).ready(function(){

	   $('#login_user').submit(function(e){
	   	   e.preventDefault()
	   	    $.ajax({


      	         url:'/auth',
      	         data:$(this).serialize(),
      	         type:'post',
      	         dataType:'json',
      	         beforeSend:function(){
      	         	$('#login_user .msg-box').html('<div class="beforesend" style="padding:30px 20px;text-algin:center"><div class="icon"><i class="text-info fa fa-spinner fa-spin" style="font-size:3.5em"></i></div><br/><h3>sending request to server</h3></div>')
                 },
      	    	     //  $('#login_user .msg-box').('<div class="beforesend" style="padding:30px 20px;text-algin:center"><div class="icon"><i class="text-info fa fa-spinner fa spin" style="font-size:3.5em"></i></div><br/><h3>sending request to server</h3></div>')
      	         
      	         success:function(data){
                        console.log(data)
      	         	if(data.status === "success"){
      	          	      $('#login_user .msg-box').html('<div class="beforesend" style="padding:30px 20px;text-algin:center"><div class="icon"><i class="text-primary fa fa-spinner fa-spin" style="font-size:3.5em"></i></div><br/><h3>'+data.success+"</div>")
      	          	      window.location="/dashboard"
      	          	}

      	          	else if(data.status === "error"){
      	          		$('#login_user .msg-box').html('<div class="beforesend" style="padding:30px 20px;text-algin:center"><div class="icon"><i class="text-danger fa fa-exclamation" style="font-size:3.5em"></i></div><br/><h3>'+data.error+"</div>")

      	          	}

      	        },
      	        error:function(){
      	        	$('#login_user .msg-box').html('<div class="beforesend" style="padding:30px 20px;text-algin:center"><div class="icon"><i class="text-info fa fa-exclamation-triangle fa spin" style="font-size:3.5em"></i></div><br/><h3>network timeout</div>')

      	        }



            })
	   })
})