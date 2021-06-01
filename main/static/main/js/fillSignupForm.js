(function() {
    const form = document.querySelector('.create-student-form');
    if (localStorage.getItem('applicationDataArr')) {
        let applicationDataArr = JSON.parse(localStorage.getItem('applicationDataArr'));

        if (form) {
            const inputs = form.querySelectorAll('.modal-form__input-container input');
            for (let item of applicationDataArr) {
                for (let input of inputs) {
                    if (input.id == item[0]) {
                        input.value = item[1].trim();
                        input.parentNode.classList.add('focus');
                    }
                }
            }
            localStorage.removeItem('applicationDataArr');
        }

    }

})();