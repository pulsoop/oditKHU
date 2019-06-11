function test(){
  var param = $("form[name=form1]").serialize();

 $.ajax({   
    type: "POST",
    url: "/test.do",
    data: param,
    success:function(data){
      alert("성공");
    },
    error:function(data){
      alert("error");
    }
  });
} 