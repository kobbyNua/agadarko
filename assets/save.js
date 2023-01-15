


forms=(form_id,urls)=>{

      $.ajax({


      	    url:urls,
      	    data:$(form_id).serialize(),
      	    type:'post',
      	    dataType:'json',
      	    beforSend:function(){
      	    	console.log('sending...')
      	    },
      	    success:function(data){
      	    	console.log(data)
      	    },
      	    error:function(){
      	    	console.log('network timeout...')
      	    }



}