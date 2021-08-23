let d=document.querySelector('.myDiv');
let centerX=document.documentElement.clientWidth/2-d.clientWidth/2;
let centerY=document.documentElement.clientHeight/2-d.clientHeight/2;
d.style.left=`${centerX}px`;
d.style.top=`${centerY}px`;