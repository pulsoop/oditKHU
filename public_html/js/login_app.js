const formEl = document.querySelector(`form`);
formEl.addEventListener(`submit`, (e) => {
  e.preventDefault();

  //콘솔로 받은 값 확인
  var user_input_id = $('input[name=id]').val();
  var user_input_pw = $('input[name=password]').val();
  console.log(user_input_id);
  console.log(user_input_pw);

  //axios를 이용해 post형식으로 서버에 정보 확인.
  axios.post("/api/signin", {
    id: $('input[name=id]').val(),
    password: $('input[name=password]').val()
  })
    //성공시 logged_in.html로 redirect
    .then(function (response) {
      if(response.status == 200)
      {
        console.log(response);
        console.log("success");
        location.href = "../index.html";
      }      
    })
    //실패시 페이지 reload
    .catch(function (error) {
      if(error.status == 401)
      {
        console.log(error);
        console.log("fail");
        location.reload();
        alert("다시 로그인해주세요!");
      }
      
    })
});