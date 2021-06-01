(function(){
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    const slides = document.querySelectorAll('.item');

    /* Индекс слайда по умолчанию */
    let slideIndex = 1;
    showSlides(slideIndex);

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
        showSlides(slideIndex -= 1);
    });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
        showSlides(slideIndex += 1);
    });
    }


    /* Устанавливает текущий слайд */
    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    /* Основная функция слайдера */
    function showSlides(n) {
        let i;
        const slides = document.getElementsByClassName("item");
        const dots = document.getElementsByClassName("slider-dots_item");
        if (n > slides.length) {
          slideIndex = 1
        }
        if (n < 1) {
            slideIndex = slides.length
        }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        if (slides[slideIndex - 1]) {
           slides[slideIndex - 1].style.display = "block";
        }
    }

    if (slides.length < 2 && nextBtn && prevBtn) {
        nextBtn.style.display = 'none';
        prevBtn.style.display = 'none';
    }

}());