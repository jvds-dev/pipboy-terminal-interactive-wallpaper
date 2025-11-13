const theme_buttons = document.querySelectorAll('li[data-theme-target]')

theme_buttons.forEach(btn =>{
    btn.addEventListener('click', () => {
        const html = document.documentElement
        html.dataset.theme = btn.dataset.themeTarget;
        updateImage()
    })
})