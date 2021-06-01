(function(){
    const table = document.querySelector('.table');
    const sortOptions = document.querySelectorAll('.table__sort-option');

    class SortTable {
        constructor(table, column, asc = true) {
          this.table = table;
          this.column = column;
          this.asc = asc;
        }
        sortTableByColumn() {
            const directionModifier = this.asc ? 1 : -1;
            const tBody = this.table.tBodies[0];
            const rows = Array.from(tBody.querySelectorAll('tr'));

            // Sort each row
            const sortedRows = rows.sort((a, b) => {
                const aColumnText = a.querySelector(`td:nth-child(${ this.column + 1 })`).textContent.trim();
                const bColumnText = b.querySelector(`td:nth-child(${ this.column + 1 })`).textContent.trim();

                return aColumnText > bColumnText ? (1 * directionModifier) : (-1 * directionModifier);
            });

            // Remove all tr's from the table
            while(tBody.firstChild) {
                tBody.removeChild(tBody.firstChild)
            }

            // Add sorted sorted rows
            tBody.append(...sortedRows);

            // Remember the way each column is sorted
            sortOptions.forEach(th => th.classList.remove('th-sort-asc', 'th-sort-desc'));
            // table.querySelector(`.table__sort-option:nth-child(${ column + 1 })`).classList.toggle('th-sort-asc', asc);
            // table.querySelector(`.table__sort-option:nth-child(${ column + 1 })`).classList.toggle('th-sort-desc', !asc);

            for (let i=0; i<this.table.querySelectorAll('.table__sort-option').length; i++) {
                if (i == this.column) {
                    this.table.querySelectorAll('.table__sort-option')[i].classList.toggle('th-sort-asc', this.asc);
                }
            }
            for (let i=0; i<this.table.querySelectorAll('.table__sort-option').length; i++) {
                if (i == this.column) {
                    this.table.querySelectorAll('.table__sort-option')[i].classList.toggle('th-sort-desc', !this.asc);
                }
            }
        }
    }


    sortOptions.forEach(header => {
        header.addEventListener('click', () => {
            const tableElement = header.closest('.table');
            const tableElementDate = header.closest('.table-date');
            const headerIndex = Array.prototype.indexOf.call(sortOptions, header);
            const currentAsc = header.classList.contains('th-sort-asc');
            const currentDesc = header.classList.contains('th-sort-desc');

            if (tableElement) {
                const nonDateTable = new SortTable(tableElement, headerIndex, !currentAsc);
                nonDateTable.sortTableByColumn();
            }
            if (tableElementDate) {
                const dateTable = new SortTable(tableElementDate, headerIndex, currentDesc);
                dateTable.sortTableByColumn();
            }
        });
    });


    if (document.querySelector('.table__sort-option--default')) {
        document.querySelector('.table__sort-option--default').click();
    }
})();
















