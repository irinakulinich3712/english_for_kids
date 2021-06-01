
(function(){
    if (document.querySelector('.alert p') && document.querySelector('.alert')) {
        const alertMsg = document.querySelector('.alert p').textContent;
        const alertItem = document.querySelector('.alert');
        const alertType = alertItem.id;

        const hideAlert = () => {
          const el = document.querySelector('.alert-final');
          if (el) el.parentElement.removeChild(el);
          deleteInitAlert();
        };

        const showAlert = (msg, type) => {
          hideAlert();
          const markup = `<div class="alert-final alert-final--${type}">${msg}</div>`;
          document.querySelector('body').insertAdjacentHTML('afterbegin', markup);
          window.setTimeout(hideAlert, 3000);
        };

        if(alertMsg) {
           showAlert(alertMsg, alertType);
        }

        function deleteInitAlert() {
           const alerts = document.querySelectorAll('.alert');
           for (let item of alerts) {
            item.remove();
           }
        }
    }
})();