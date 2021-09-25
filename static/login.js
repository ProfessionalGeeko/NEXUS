const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const success = document.getElementById('success')
const danger = document.getElementById('danger 1')

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

function successcheck() {
<<<<<<< HEAD

=======
	 
>>>>>>> c6cd488b611bb765fd4f75edff2369f6efc2bfdb
	if (success) {
		container.classList.remove("right-panel-active");
		print('done')
}
	if (danger) {
		if (op != 'None'){
			document.getElementById('un').classList.add('form-control')
			document.getElementById('un').classList.add('is-invalid')
		}
		if (op1 != 'None'){
			document.getElementById('up').classList.add('form-control')
			document.getElementById('up').classList.add('is-invalid')
		}
		container.classList.add("right-panel-active");
}
}

successcheck()
console.log(op)