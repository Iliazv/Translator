let modal = document.getElementById('modal');
let overlay = document.getElementById('overlay');

function openModal() {
    modal.classList.add('open-modal');
    overlay.classList.add('active')
}

function closeModal() {
    modal.classList.remove('open-modal');
    overlay.classList.remove('active')
}

function changePic() {
    document.getElementById("star").src = "../static/vega/images/star-active.png";
}