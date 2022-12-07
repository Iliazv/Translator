let sidebar = document.getElementById('sidebar');
let side = document.getElementById('side');

const screenWidth = window.screen.width
const screenHeight = window.screen.height

function openSidebar() {
    if (side.classList.contains('active')) {
        closeSide()
    }

    sidebar.classList.add('active');
    if (screenWidth > 1350) {
        document.querySelector('.content').style.margin = '0 0 0 -400px';
        document.querySelector('.header').style.margin = '0 0 0 400px';
    }

    else if (screenWidth > 1050) {
        document.querySelector('.content').style.margin = '0 0 0 -300px';
        document.querySelector('.header').style.margin = '0 0 0 300px';
    }

    else if (screenWidth > 800) {
        document.querySelector('.content').style.margin = '0 0 0 -260px';
        document.querySelector('.header').style.margin = '0 0 0 260px';
    }

    else {
        document.querySelector('.content').style.margin = '0 0 0 -220px';
        document.querySelector('.header').style.margin = '0 0 0 220px';
    }
}

function closeSidebar() {
    sidebar.classList.remove('active');
    document.querySelector('.content').style.margin = '0 0 0 0';
    document.querySelector('.header').style.margin = '0 0 0 0';
}

function openSide() {
    if (sidebar.classList.contains('active')) {
        closeSidebar()
    }

    side.classList.add('active');
    if (screenWidth > 1350) {
        document.querySelector('.content').style.margin = '0 0 0 -400px';
        document.querySelector('.header').style.margin = '0 0 0 400px';
    }

    else if (screenWidth > 1050) {
        document.querySelector('.content').style.margin = '0 0 0 -300px';
        document.querySelector('.header').style.margin = '0 0 0 300px';
    }

    else if (screenWidth > 800) {
        document.querySelector('.content').style.margin = '0 0 0 -260px';
        document.querySelector('.header').style.margin = '0 0 0 260px';
    }

    else {
        document.querySelector('.content').style.margin = '0 0 0 -220px';
        document.querySelector('.header').style.margin = '0 0 0 220px';
    }
}

function closeSide() {
    side.classList.remove('active');
    document.querySelector('.content').style.margin = '0 0 0 0';
    document.querySelector('.header').style.margin = '0 0 0 0';
}