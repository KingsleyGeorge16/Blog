//var sidemenu = document.getElementById("sidemenu");
//
//function openmenu(){
//    sidemenu.style.right = "0";
//}
//function closemenu() {
//    sidemenu.style.right = "-200px";
//}

const bar = document.getElementById('bar');
const close = document.getElementById('close');
const side = document.getElementById('sidemenu');

if (bar) {
    bar.addEventListener('click', () => {
        side.classList.add('active');
    })
}

if (close) {
    close.addEventListener('click', () => {
        side.classList.remove('active');
    })
}