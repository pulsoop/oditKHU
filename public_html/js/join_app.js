const formEl = document.querySelector(`form`);
formEl.addEventListener(`submit`, (e) => {
	e.preventDefault();

	//콘솔로 받은 값 확인
	var user_id = $('input[name=id]').val();
	var user_name = $('input[name=name]').val();
	var user_pw = $('input[name=password]').val();
	var user_email = $('input[name=email]').val();
	var user_phone = $('input[name=phone]').val();
	console.log(user_id);
	console.log(user_name);
	console.log(user_pw);
	console.log(user_email);
	console.log(user_phone);

	//axios를 이용해 post형식으로 서버에 정보 확인.
	axios.post("/api/signup", {
		id: $('input[name=id]').val(),
		password: $('input[name=password]').val(),
		name: $('input[name=name]').val(),
		email: $('input[name=email]').val(),
		phone: $('input[name=phone]').val()
	})
		.then(function (response) {
			if(response.status == 200)
			{
				console.log(response);
				console.log("success");
				location.href = "./login.html";
			}
		})
		//실패시 페이지 reload
		.catch(function (error) {
			if(error.status != 200)
			{
				console.log(error);
				console.log("fail");
			}
		})
});