(function() {
    const search = document.querySelector('.search-input');
    const searchedData = document.querySelectorAll('.searched-data');
    const searchClear = document.querySelector('.search-clear');

    if (search) {
        search.addEventListener('input', (e) => {
            let val = e.currentTarget.value;
            if (val != '') {
                searchedData.forEach(elem => {
                    let elemArr = elem.textContent.split(' ');
                    let regex = new RegExp(`^${val}`, 'gi');
                    if (elemArr.length == 1) {
                        if (elemArr[0].match(regex)) {
                            elem.parentElement.classList.remove('hide');
                        }
                        else {
                            elem.parentElement.classList.add('hide');
                        }
                    }
                    else {
                        if (elemArr[0].match(regex) || elemArr[1].match(regex)) {
                            elem.parentElement.classList.remove('hide');
                        }
                        else {
                        elem.parentElement.classList.add('hide');
                        }
                    }
                });
            }
            else {
                searchedData.forEach(elem => {
                    elem.parentElement.classList.remove('hide');
                });
            }
        });
    }

    if (searchClear) {
        searchClear.addEventListener('click', () => {
            search.value = '';
            searchedData.forEach(elem => {
                elem.parentElement.classList.remove('hide');
                elem.innerHTML = elem.innerText;
            });
        });
    }
})();