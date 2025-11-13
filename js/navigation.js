const buttons = document.querySelectorAll('button[data-page]')
const pages = document.querySelectorAll('.page')

buttons.forEach(btn => {
    btn.addEventListener('click', () => {
        buttons.forEach(inactiveBtn => {
            if(inactiveBtn !== btn){
                inactiveBtn.classList.remove('active')
            }
            else{
                btn.classList.add('active')        
            }
        })
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