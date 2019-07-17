$(document).ready(function(){

		$("#login-submit-button").click(function(ev){

			ev.preventDefault();
			if(!$("#login-email").val()){
				$("#login-email").parent().addClass("has-error");
				return;
			} else {
				$("#login-email").parent().removeClass("has-error");
			}

			if(!$("#login-password").val()){
				$("#login-password").parent().addClass("has-error");
				return;
			} else {
				$("#login-password").parent().removeClass("has-error");
			}

			$("#login-form").submit();

		});

		$("#register-submit-button").click(function(ev){

			ev.preventDefault();
	//Password and email authentication
			var email=$("#register-email").val();
			var pass=$("#register-password").val();

			var email_regex=/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
			var minNumberofChars = 6;
			var maxNumberofChars = 16;
			var password_regex  = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;

			if(pass.length < minNumberofChars){
				$("#register-password").parent().addClass("has-error");
				$("#register-passwd-error4").show();
				//alert("Please Enter Strong Password");
				return;
			}else{
				$("#register-password").parent().removeClass("has-error");
				$("#register-passwd-error4").hide();
			}
			if(pass.length > maxNumberofChars){
				$("#register-password").parent().addClass("has-error");
				$("#register-passwd-error4").show();
				//alert("Please Enter Strong Password");
				return;
			}else{
				$("#register-password").parent().removeClass("has-error");
				$("#register-passwd-error4").hide();
			}
			if(password_regex.test(pass)==false){
				$("#register-password").parent().addClass("has-error");
				$("#register-passwd-error4").show();
				//alert("Please Enter Strong Password");
				return;
			}else{
				$("#register-password").parent().removeClass("has-error");
				$("#register-passwd-error4").hide();
			}


			if(email_regex.test(email)==false){
				$("#register-email").parent().addClass("has-error");
				$("#register-invalidemail-error").show();
				//alert("Please Enter Correct Email");
				return;
			}else{
				$("#register-email").parent().removeClass("has-error");
				$("#register-invalidemail-error").hide();
			}

	//shows error if there is no email address
			if(!$("#register-email").val()){
				$("#register-email").parent().addClass("has-error");
				$("#register-email-error").show();
				return;
			} else {
				$("#register-email").parent().removeClass("has-error");
				$("#register-email-error").hide();
			}
	//shows error if 1st password is not given
			if(!$("#register-password").val()){
				$("#register-password").parent().addClass("has-error");
				$("#register-passwd-error2").show();
				return;
			} else {
				$("#register-password").parent().removeClass("has-error");
				$("#register-passwd-error2").hide();
			}
	//shows error message if password is NOT entered a second time
			if(!$("#register-password2").val()){
				$("#register-password2").parent().addClass("has-error");
				$("#register-passwd-error3").show();
				return;
			} else {
				$("#register-password2").parent().removeClass("has-error");
				$("#register-passwd-error3").hide();
			}
	//shows error if passwords are not equal
			if($("#register-password").val() != $("#register-password2").val()){
				$("#register-password").parent().addClass("has-error");
				$("#register-password2").parent().addClass("has-error");
				$("#register-passwd-error").show();
				return;
			} else {
				$("#register-password").parent().removeClass("has-error");
				$("#register-password2").parent().addClass("has-error");
				$("#register-passwd-error").hide();
			}

			$("#register-form").submit();

		});

		// Function that validates email address through a regular expression.
		function validateEmail(sEmail) {
			var filter = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
			if (filter.test(sEmail)==true) {
			return true;
			}
			else {
			return false;
			}
			}

		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}
	});

	Storage.prototype.setObject = function(key, value) {
		this.setItem(key, JSON.stringify(value));
	};

	Storage.prototype.getObject = function(key) {
		return JSON.parse(this.getItem(key));
	};
