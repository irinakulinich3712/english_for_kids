(function(){
    sortBtn = document.querySelector('.data-card__sort-btn');

    class SortNonTable {
      constructor(dataCardSection, sortOption, asc = true) {
        this.dataCardSection = dataCardSection;
        this.sortOption = sortOption;
        this.asc = asc;
      }
      sortDataCards() {
          const directionModifier = this.asc ? 1 : -1;
          const dataBlock = this.dataCardSection.querySelectorAll('.data-card__card');
          const dataBlocks = Array.from(dataBlock);


          const sortedBlocks = dataBlocks.sort((a, b) => {
              const aDataBlocks = new Date(a.querySelector(`.${this.sortOption} aside span`).textContent.trim());
              const bDataBlocks = new Date(b.querySelector(`.${this.sortOption} aside span`).textContent.trim());

              return aDataBlocks > bDataBlocks ? (1 * directionModifier) : (-1 * directionModifier);
          });


          while(this.dataCardSection.firstChild) {
            this.dataCardSection.removeChild(this.dataCardSection.firstChild)
          }

          this.dataCardSection.append(...sortedBlocks);

          sortBtn.classList.remove('th-sort-asc', 'th-sort-desc');
          sortBtn.classList.toggle('th-sort-asc', this.asc);
          sortBtn.classList.toggle('th-sort-desc', !this.asc);
      }
    }


    if (sortBtn && document.querySelector('.data-card__section')) {
         sortBtn.addEventListener('click', () => {
        const dataCardSection = document.querySelector('.data-card__section');
        const currentDesc = sortBtn.classList.contains('th-sort-desc');
        const nonTable = new SortNonTable(dataCardSection, 'data-card__card-top-visible', currentDesc);
        nonTable.sortDataCards();
    });
    }

    if (sortBtn && document.querySelector('.data-card__section')) {
       sortBtn.click();
    }
}());