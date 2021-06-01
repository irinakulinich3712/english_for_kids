(function(){
    const inputs = document.querySelectorAll(".form__input");

    function addcl(input) {
      let parent = input.parentNode.parentNode;
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
      if (input.value != '') {
        addcl(input);
      }
    });
})();