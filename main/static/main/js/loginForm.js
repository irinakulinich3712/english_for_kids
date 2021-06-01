(function(){
    const inputs = document.querySelectorAll(".form__input");
    const passBlock = document.querySelector(".pass");
    const emailInput = document.querySelector("#email");

    function addcl() {
        let parent = this.parentNode.parentNode;
        parent.classList.add("focus");
    }

    function remcl() {
        let parent = this.parentNode.parentNode;
        if (this.value == "") {
            parent.classList.remove("focus");
        }
    }

    inputs.forEach((input) => {
        input.addEventListener("focus", addcl);
        input.addEventListener("blur", remcl);
    });
    if (emailInput) {
        if (emailInput.value != '') {
        emailInput.closest('.input-div').classList.add("focus");
    }
    }


})();