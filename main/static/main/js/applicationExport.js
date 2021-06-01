(function() {
    const applicationExport = document.querySelector('.application-export');
    const applicationData = document.querySelectorAll('.application-data');
    const signupInputs = document.querySelectorAll('.signup-form__input');

    if (applicationExport) {
        applicationExport.addEventListener('click', () => {
            let applicationDataArr = []

            for (let dataItem of applicationData) {
                let dataItemArr = [dataItem.getAttribute('data-td'), dataItem.textContent];
                applicationDataArr.push(dataItemArr);
            }
            localStorage.setItem('applicationDataArr', JSON.stringify(applicationDataArr));
             window.location.assign('/students/new-student/');
        });
    }
})();

