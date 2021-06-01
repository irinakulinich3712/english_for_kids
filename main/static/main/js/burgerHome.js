(function(){
      const menuList = document.querySelector('.navbar__menu-list');
      const menuBtn = document.querySelector('.navbar__icon-menu-btn');
      const cancelBtn = document.querySelector('.navbar__icon-cancel-btn');
      const menuLinks = document.querySelectorAll('.navbar__menu-link');

      const navSlide = () => {
      // thoggle menu
        if (menuBtn) {
            menuBtn.addEventListener('click', () => {
            menuList.classList.add('navbar--active');

            menuLinks.forEach((link, index) => {
              if (!link.style.animation) {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + .5}s`;
              }
            });
          })
      }

      if (cancelBtn) {
        cancelBtn.addEventListener('click', () => {
            menuList.classList.remove('navbar--active');
            for (let link of menuLinks) {
                link.style.animation = '';
            }
        });
      }


    }

    navSlide();

}());