export default function menu(div,btn) {

        const $menu = document.querySelector(div),
                    $hamburger = document.querySelectorAll(btn);


                document.addEventListener('click', (e) => {
                    console.log(e.target.matches)
                    if(e.target.matches(`${btn} *`)) $menu.classList.toggle('is-active')
                })

    }