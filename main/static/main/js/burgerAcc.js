
(function(){

      const navSlide = () => {

        if (document.querySelector('.sidebar__icon-menu-btn')) {
            document.querySelector('.sidebar__icon-menu-btn').addEventListener('click', () => {
            document.querySelector('.sidebar').classList.add('sidebar--active');
        })
        }


        if (document.querySelector('.sidebar__icon-cancel-btn')) {
            document.querySelector('.sidebar__icon-cancel-btn').addEventListener('click', () => {
            document.querySelector('.sidebar').classList.remove('sidebar--active');
        });
        }




    }

    navSlide();

}());