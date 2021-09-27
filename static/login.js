const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const danger = document.getElementsByClassName('invalid-feedback');
const user_error = document.getElementById('username');
const pass_error = document.getElementById('password');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function successcheck() {
	if (danger.length != 0) {
		container.classList.add("right-panel-active");
		if (user_error){
			console.log('usernameerror')
			document.getElementById('un').classList.add("form-control");
			document.getElementById('un').classList.add("is-invalid");
		}
		if (pass_error){
			console.log('passworderror')
			document.getElementById('up').classList.add("form-control");
			document.getElementById('up').classList.add("is-invalid");
			document.getElementById('up1').classList.add("form-control");
			document.getElementById('up1').classList.add("is-invalid");
		}
	}
	else {
			container.classList.remove("right-panel-active");
	}
}

successcheck()