let header=document.querySelector('.header');


function changeBg(){
    
    header.classList.toggle('header-second');
}
setInterval(changeBg,4000);

