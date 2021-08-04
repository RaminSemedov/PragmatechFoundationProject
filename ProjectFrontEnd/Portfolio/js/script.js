
const header=document.querySelector('.header');
const info=document.querySelector('.info');
const first= document.querySelector('.header-info-firs');
const second=document.querySelector('.header-info-second');
const circles=document.querySelectorAll('.inner-circle');

const nav=document.querySelector('.header-navigation');

const expCounter=document.querySelector('.experience h2');




function changeBg(){    
    header.classList.toggle('header-second');   
}

let flag=true;
function changeText(){
     if(flag){
        first.style.display='block';
        second.style.display='none';
        circles[0].classList.add('active-circle');
        circles[1].classList.remove('active-circle');
        flag=false;
     }
     else{
        first.style.display='none';
        second.style.display='block';
        circles[0].classList.remove('active-circle');
        circles[1].classList.add('active-circle');
        flag=true; 
     }       
   
}
changeText();
setInterval(changeBg,4000);
setInterval(changeText,4000);


let counter=1;
function countYears(){
   expCounter.innerHTML=counter;
   if(counter<42)
   counter++;
}

window.addEventListener("scroll",()=>{
   if(window.scrollY>1260){
      setInterval(countYears,300);   
   }
})
