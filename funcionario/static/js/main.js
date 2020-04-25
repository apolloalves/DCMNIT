'use-strict'

document.addEventListener('DOMContentLoaded', () => {
    let elems = document.querySelectorAll( '.tooltipped' );
    let sidenav = document.querySelectorAll( '.sidenav' );
    let instances = M.Tooltip.init( elems,{enterDelay: 300,exitDelay:100} );
    let instance = M.Sidenav.init( sidenav );

});

