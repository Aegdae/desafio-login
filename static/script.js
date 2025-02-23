function togglePassword(fieldId, iconId) {
    let field = document.getElementById(fieldId);
    let eyesIcon = document.getElementById(iconId);
    
    if (field.type === "password") {
        field.type = "text";
        eyesIcon.classList.remove("fa-eye");
        eyesIcon.classList.add("fa-eye-slash");
    } else {
        field.type = "password";
        eyesIcon.classList.remove("fa-eye-slash");
        eyesIcon.classList.add("fa-eye");
    }
}


document.addEventListener('DOMContentLoaded', function () {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const submitButton = document.getElementById('loginBtn');

    function checkFormValidityLogin() {
        if (emailInput.value.trim() !== '' && passwordInput.value.trim() !== '') {
            submitButton.disabled = false;
            submitButton.style.background = "#007bff"
            submitButton.style.color = '#fff';
            submitButton.style.opacity = '1';
            submitButton.style.cursor = "pointer"

        } else {
            submitButton.disabled = true;  
            submitButton.style.backgroundColor = '#ccc'; 
            submitButton.style.color = '#666';
            submitButton.style.opacity = '0.6';
            submitButton.style.cursor = "default"
        }
    }

    emailInput.addEventListener('input', checkFormValidityLogin);
    passwordInput.addEventListener('input', checkFormValidityLogin);
    checkFormValidityLogin(); 
});


document.addEventListener('DOMContentLoaded', function () {
    const nameInput = document.getElementById("first_name")
    const emailInput = document.getElementById('email');
    const password1Input = document.getElementById('password1');
    const password2Input = document.getElementById('password2');
    const submitButton = document.getElementById('registerBtn');

    function checkFormValidityRegister() {
        if (nameInput.value.trim() !== '' && emailInput.value.trim() !== '' && password1Input.value.trim() !== '' && password2Input.value.trim() !== '') {
            submitButton.disabled = false;
            submitButton.style.background = "#007bff"
            submitButton.style.color = '#fff';
            submitButton.style.opacity = '1';
            submitButton.style.cursor = "pointer"

        } else {
            submitButton.disabled = true;  
            submitButton.style.backgroundColor = '#ccc'; 
            submitButton.style.color = '#666';
            submitButton.style.opacity = '0.6';
            submitButton.style.cursor = "default"
        }
    }

    nameInput.addEventListener('input', checkFormValidityRegister);
    emailInput.addEventListener('input', checkFormValidityRegister);
    password1Input.addEventListener('input', checkFormValidityRegister);
    password2Input.addEventListener('input', checkFormValidityRegister);
    checkFormValidityRegister()
})