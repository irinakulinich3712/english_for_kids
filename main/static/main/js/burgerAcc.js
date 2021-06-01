
(function(){

      const navSlide = () => {

        if (document.querySelector('.sidebar__icon-menu-btn')) {
            document.querySelector('.sidebar__icon-menu-btn').addEventListener('click', () => {
            document.querySelector('.sidebar').classList.add('sidebar--active');
            document.querySelector('.sidebar__icon-menu-btn').classList.add('sidebar__icon-menu-btn--hide');
        })
        }


        if (document.querySelector('.sidebar__icon-cancel-btn')) {
            document.querySelector('.sidebar__icon-cancel-btn').addEventListener('click', () => {
            document.querySelector('.sidebar').classList.remove('sidebar--active');
            document.querySelector('.sidebar__icon-menu-btn').classList.remove('sidebar__icon-menu-btn--hide');
        });
        }




    }

    navSlide();

}());
