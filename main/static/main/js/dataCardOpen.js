(function(){
    const dataCardBtns = document.querySelectorAll('.data-card__card-top-btn');
    const topCardHidden = document.querySelector('.data-card__card-top-hidden');
    const bottomCard = document.querySelector('.data-card__card-bottom');

    dataCardBtns.forEach( btn => {
      btn.addEventListener('click', () => {
        btn.classList.toggle('active');
        btn.closest('.data-card__card').querySelector('.data-card__card-top-hidden').classList.toggle('active');
        btn.closest('.data-card__card').querySelector('.data-card__card-bottom').classList.toggle('active');
      });
    });
})();