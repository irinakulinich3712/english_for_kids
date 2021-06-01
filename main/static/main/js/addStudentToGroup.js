(function(){
    const searchStudentsAutocomplete = document.querySelector('#search-students-autocomplete');
    const matchList = document.querySelector('.match-list');
    const searchClear = document.querySelector('.search-clear--hidden');
    const studentAddWindow = document.querySelector('.data-card__student-add-window');
    const addStudentBtn = document.querySelector('.data-card__student-add-btn')
    const declineStudentBtn = document.querySelector('.data-card__student-dec-btn')


    let matches;
    const searchStudents = async searchText => {

        try {
            let temp = [];
            let temp2 = [];
            let students = [];
            const res = await fetch('http://127.0.0.1:8000/choose-student/');
            const data = await res.text();
            const arr = data.slice(1,-1).split('}{');
            for (let i of arr) {
                let item = i.split(',');
                    for (let elem of item) {
                        temp.push(elem.split(':'));
                    }
            }
            for (let i=0; i<temp.length; i+=5) {
                if(temp[i] != undefined && temp[i+1] != undefined && temp[i+2] != undefined
                && temp[i+3] != undefined && temp[i+4] != undefined) {
                    temp2.push([temp[i], temp[i+1], temp[i+2], temp[i+3], temp[i+4]]);
                }
            }

            for (let item of temp2) {
                let a = String(item[0][1]).trim()
                let b = String(item[1][1]).trim().slice(1,-1);
                let c = String(item[2][1]).trim().slice(1,-1);
                let d = String(item[3][1]).trim();
                let e = String(item[4][1]).trim().slice(1,-1);;
                let obj = {
                    user_id: a,
                    user__last_name: b,
                    user__first_name: c,
                    student_group_id: d,
                    student_group: e
                }
                students.push(obj);

            }

            matches = students.filter(student => {
                const regex = new RegExp(`^${searchText}`, 'gi');
                return student.user__first_name.match(regex) || student.user__last_name.match(regex);
            });
            if (searchText.length === 0) {
                matches = [];
                matchList.innerHTML = '';
            }
            outputHtml(matches);
            addStudentToGroup();
        } catch (err) {
        }
    }

    const outputHtml = matches => {
        const htmlResults = matches.map(match => {
            if (match.student_group_id != addStudentBtn.getAttribute('data-group-add-id')) {
                return `<div class="match-item">
                    <span data-student-id="${match.user_id}">${match.user__last_name} ${match.user__first_name}</span>
                    <span>Current group: ${match.student_group}</span>
                </div>`
            }
        }).join('');

        matchList.innerHTML = htmlResults; 
        matchList.getElementsByClassName.backgroundColor="black"; 
    }

    const addStudentToGroup = () => {
        if (matchList.innerHTML != '') {
            const students = matchList.querySelectorAll('.match-item')
            students.forEach(item => {
                item.addEventListener('click', () => {
                    searchStudentsAutocomplete.value = item.firstElementChild.textContent;
                    matches = [];
                    matchList.innerHTML = '';
                    searchStudentsAutocomplete.value = '';
                    addStudentBtn.setAttribute('data-student-add-id', item.firstElementChild.getAttribute('data-student-id'));
                    studentAddWindow.firstElementChild.textContent = item.firstElementChild.textContent;
                    studentAddWindow.classList.add('data-card__student-add-window--show');
                });
            });
        }
    }

    if (declineStudentBtn) {
        declineStudentBtn.addEventListener('click', () => {
        studentAddWindow.classList.remove('data-card__student-add-window--show');
    });
    }



    const addStudent = async (groupId, studentId) => {
        try {
            const res = await fetch(`http://127.0.0.1:8000/groups/${groupId}/students/add-student/${studentId}/`);
            document.location.reload();
        } catch (err) {
        }  
    };

    if (addStudentBtn) {
        addStudentBtn.addEventListener('click', () => {
        const groupId = addStudentBtn.getAttribute('data-group-add-id');
        const studentId = addStudentBtn.getAttribute('data-student-add-id');
        addStudent(groupId, studentId);
        });
    }



    

    if (searchClear) {
        searchClear.addEventListener('click', () => {
            searchStudentsAutocomplete.value = '';
            matchList.innerHTML = '';
            matches = [];
        });
    }

    

    // Adding event to search input 

    if (searchStudentsAutocomplete) {
        searchStudentsAutocomplete.addEventListener('input', () => searchStudents(searchStudentsAutocomplete.value));
    }    
})();



