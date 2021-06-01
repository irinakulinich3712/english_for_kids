(function(){
class TabController {
    constructor(tabElement, tabelementClass) {
        this.tabElement = tabElement;
        this.tabelementClass = tabelementClass;
    }
    
    manageTab() {
        this.tabElement.forEach(item => {
            item.addEventListener('click', () => {
                localStorage.setItem('item-active', item.id);
            });
        });

        if (localStorage.getItem('item-active')) {
            const itemActive = localStorage.getItem('item-active');
            for (let item of  this.tabElement) {
                if (item.id == itemActive) {
                    item.parentElement.classList.add(this.tabelementClass);
                }
            }
            localStorage.removeItem('item-active');
        }
    
        for (let item of this.tabElement) {
            if (item.href == window.location.href) {
                item.parentElement.classList.add(this.tabelementClass);
            }
            if (window.location.href == `${item.href}?` || window.location.href == `${item.href}/`) {
                item.parentElement.classList.add(this.tabelementClass);
                window.location.href = item.href;
            }
        }
    }
}

const sideBarTab = new TabController(document.querySelectorAll('.sidebar-menu__link'), 'sidebar-menu__item--active');
sideBarTab.manageTab();

const dataCardTab = new TabController(document.querySelectorAll('.data-card__nav-item-link'), 'data-card__nav-item--active');
dataCardTab.manageTab();
})();