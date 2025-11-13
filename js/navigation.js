const buttons = document.querySelectorAll('button[data-page]')
const pages = document.querySelectorAll('.page')

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        showPage(btn.dataset.page)
    })
});

function showPage(pageName){
    pages.forEach(page => {
        if(page.dataset.page === pageName){
            page.classList.remove('hidden')
        }
        else{
            page.classList.add('hidden')
        }
    })
}