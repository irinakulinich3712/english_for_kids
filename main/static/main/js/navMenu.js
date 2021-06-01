(function(){
    let fullHeight = document.body.scrollHeight;
    let innerHeight = window.innerHeight;
    const progressBar = document.querySelector('.progressbar-line');

    window.addEventListener('scroll', fillProgressLine);
    window.addEventListener('resize', fillProgressLine);

    function fillProgressLine() {
      fullHeight = document.body.scrollHeight;
      innerHeight = window.innerHeight;
      if (progressBar) {
         progressBar.style.width = (pageYOffset * 100 / (fullHeight - innerHeight)) + '%';
      }
    }
}());









