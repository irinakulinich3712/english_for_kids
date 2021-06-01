(function(){
    const modalTrigger = document.querySelectorAll('.md-trigger');
    const modalClose = document.querySelectorAll('.md-close');
    const modalWindow = document.querySelector('.md-modal');
    const editInputs = document.querySelectorAll('.modal-form__input');
    const modalForm = document.querySelector('.modal-form');
    const modalEditForm = document.querySelector('.modal-form-edit');
    const modalCreateForm = document.querySelector('.modal-form-create');
    const modalConfirmForm = document.querySelector('.modal-form-confirm');


    modalTrigger.forEach(modalBtn => {
        modalBtn.addEventListener('click', () => {
            modalWindow.classList.add('md-show');
            createHeader(modalBtn);
            if (modalBtn.classList.contains('create-flag')) {
                if (modalEditForm) {
                    modalEditForm.classList.remove('modal-form-visible');
                }
                if (modalConfirmForm) {
                    modalConfirmForm.classList.remove('modal-form-visible');
                }
                modalCreateForm.classList.add('modal-form-visible');
            }
            if (modalBtn.classList.contains('edit-flag')) {
                if (modalCreateForm) {
                    modalCreateForm.classList.remove('modal-form-visible');
                }
                if (modalConfirmForm) {
                    modalConfirmForm.classList.remove('modal-form-visible');
                }
                modalEditForm.classList.add('modal-form-visible');
                editData(modalBtn);
                formUrl(modalBtn);
            }
             if (modalBtn.classList.contains('delete-flag')) {
                if (modalCreateForm) {
                    modalCreateForm.classList.remove('modal-form-visible');
                }
                if (modalEditForm) {
                    modalEditForm.classList.remove('modal-form-visible');
                }
                modalConfirmForm.classList.add('modal-form-visible');
                deleteData(modalBtn);
            }
        });
    });

     function createHeader(modalBtn) {
        if (modalBtn.hasAttribute('data-header')) {
            modalWindow.querySelector('h2').textContent = modalBtn.getAttribute('data-header');
        }
     }


    modalClose.forEach(item => {
        item.addEventListener ('click', () => {
            modalWindow.classList.remove('md-show');
            setTimeout(() => {
                if (modalCreateForm && modalCreateForm.classList.contains('modal-form-visible')) {
                    modalCreateForm.classList.remove('modal-form-visible');
                    const formInputs = modalCreateForm.querySelectorAll('.create-form__input');
                    for (let input of formInputs) {
                        input.value = ' ';
                    }
                }
                if (modalEditForm && modalEditForm.classList.contains('modal-form-visible')) {
                    modalEditForm.classList.remove('modal-form-visible');
                    const formInputs = modalEditForm.querySelectorAll('.create-form__input');
                    for (let input of formInputs) {
                        input.value = ' ';
                    }
                }
            }, 250);

        });
    });


    function editData(modalBtn) {
            const editedData = modalBtn.closest('.data-card__card').querySelectorAll('.data-card__data-edit');
            for (let item of editedData) {
                 for (let input of editInputs) {
                     if (item.getAttribute('data-edit') == input.id) {
                         input.value = item.textContent;
                     }
                 }
            }

    }

    function formUrl(modalBtn) {
        if (modalBtn.hasAttribute('data-lesson-id')) {
            const lessonId = modalBtn.getAttribute('data-lesson-id');
            const groupId = modalBtn.getAttribute('data-group-id');
            modalEditForm.setAttribute('action', `/groups/${groupId}/lessons/edit-lesson/${lessonId}/`)
        }
        else if(modalBtn.hasAttribute('data-observation-id'))  {
            const observationId = modalBtn.getAttribute('data-observation-id');
            const studentId = modalBtn.getAttribute('data-student-id');
            modalEditForm.setAttribute('action', `/students/${studentId}/edit-observation/${observationId}/`)
        }
        else if(modalBtn.hasAttribute('data-announcement-id'))  {
            const announcementId = modalBtn.getAttribute('data-announcement-id');
            modalEditForm.setAttribute('action', `/announcements/edit-announcement/${announcementId}/`)
        }
    }

    function deleteData(modalBtn) {
         if(modalBtn.hasAttribute('data-announcement-delete-id')) {
            const deleteAnnouncementId = modalBtn.getAttribute('data-announcement-delete-id')
            document.querySelector('.md-delete-data a').href = `/announcements/delete-announcement/${deleteAnnouncementId}/`
        }
        if(modalBtn.hasAttribute('data-lesson-delete-id')) {
            const deleteLessonId = modalBtn.getAttribute('data-lesson-delete-id');
            const groupId = modalBtn.getAttribute('data-group-delete-id');
            document.querySelector('.md-delete-data a').href = `/groups/${groupId}/lessons/delete-lesson/${deleteLessonId}/`
        }
        if(modalBtn.hasAttribute('data-observation-delete-id')) {
            const deleteObservationId = modalBtn.getAttribute('data-observation-delete-id');
            const studentId = modalBtn.getAttribute('data-student-delete-id');
            document.querySelector('.md-delete-data a').href = `/students/${studentId}/observation/delete-observation/${deleteObservationId}/`
        }
        if(modalBtn.hasAttribute('data-student-delete-id')) {
            const deleteStudentId = modalBtn.getAttribute('data-student-delete-id');
            document.querySelector('.md-delete-data a').href = `/students/${deleteStudentId}/delete-student/`
        }
        if(modalBtn.hasAttribute('data-group-delete-id')) {
            const deleteGroupId = modalBtn.getAttribute('data-group-delete-id');
            document.querySelector('.md-delete-data a').href = `/groups/${deleteGroupId}/delete-group/`
        }
        if(modalBtn.hasAttribute('data-application-delete-id')) {
            const deleteApplicationId = modalBtn.getAttribute('data-application-delete-id');
            document.querySelector('.md-delete-data a').href = `/applications/${deleteApplicationId}/delete-application/`
        }
    }
})();










