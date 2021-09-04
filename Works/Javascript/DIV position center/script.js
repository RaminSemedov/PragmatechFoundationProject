let d=document.querySelector('.myDiv');
window.addEventListener('resize',setInCenter);

function setInCenter(){
    let centerX=document.documentElement.clientWidth/2-d.clientWidth/2;
    let centerY=document.documentElement.clientHeight/2-d.clientHeight/2;
    d.style.left=`${centerX}px`;
    d.style.top=`${centerY}px`;
}
setInCenter();