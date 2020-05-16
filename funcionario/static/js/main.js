'use-strict'
console.warn('Desenvolvido por DCMNIT - Soluções em Tecnologias')

window.addEventListener('load', () => {
    let tooltipped = document.querySelectorAll( '.tooltipped' );
    let sidenav = document.querySelectorAll( '.sidenav' );
    
    let inst_tooltipped = M.Tooltip.init( tooltipped,{ enterDelay: 300,exitDelay:100 } );
    let inst_sidenav = M.Sidenav.init( sidenav );

    let modal = document.querySelectorAll( '.modal' );
    let inst_modal = M.Modal.init(modal);

    let modal_delete = document.querySelector( '#modal_delete' );
    let inst_modal_delete = M.Modal.init( modal_delete );
    
   
});

