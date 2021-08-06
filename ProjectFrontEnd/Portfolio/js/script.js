
const header=document.querySelector('.header');
const info=document.querySelector('.info');
const first= document.querySelector('.header-info-firs');
const second=document.querySelector('.header-info-second');
const circles=document.querySelectorAll('.inner-circle');
const nav=document.querySelector('.header-navigation');
const expCounter=document.querySelector('.experience h2');
const menuBtn=document.querySelector(".menu-btn");
const headerNavMobile=document.querySelector(".header-nav-mobile");
const projectCounter=document.querySelector(".projectCounter");
const stafCounter=document.querySelector(".stafCounter");
const serviceCounter=document.querySelector(".serviceCounter");
const constumerCounter=document.querySelector(".constumerCounter");




menuBtn.addEventListener("click",()=>{
   headerNavMobile.classList.toggle("hnm-full");

})



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
   if(document.documentElement.scrollTop>1260){
      setInterval(countYears,300);   
   }
})


// Project Counter start

let projectCount=0;
let projectCountFraction=0;

function countProjects(){
if(projectCount<5)
   projectCounter.textContent=projectCount+","+projectCountFraction;
    if(projectCountFraction==980){
       projectCount++;
       projectCountFraction=0;       
    }  
    projectCountFraction+=20;
    if(projectCount==4){
      projectCountFraction=800;
   }

   
}
// Project counter end

// Staf counter start
let stafCount=0;
let stafCountFraction=0;

function countStaf(){
   if(stafCount<1)
   stafCountFraction+=3;
   stafCounter.textContent=stafCountFraction;
   if(stafCountFraction==999){
      stafCount=1;
      stafCountFraction="000";     
      
   }  
   if(stafCount==1){
      stafCounter.textContent=stafCount+ "," +stafCountFraction;
   }
    
   
}
// Staf counter end
// Service counter start
let serviceCount=0;

function countService(){
if(serviceCount<350){
   serviceCount++;
   serviceCounter.textContent=serviceCount;
}
}
// Service counter end
// Costumer counter start
let costumerCount=0;
let costumerCountFraction=0;

function countCostumers(){
if(costumerCount<8)
    constumerCounter.textContent=costumerCount+","+costumerCountFraction;
    if(costumerCountFraction==990){
       costumerCount++;
       costumerCountFraction=0;       
    }  
    costumerCountFraction+=30;
    if(costumerCount==7){
      costumerCountFraction=650;
   }

   
}


// Costumet copunter end

 function callCounters(){
    countProjects();
    countStaf();
    countService();
    countCostumers();

 }

window.addEventListener("scroll",()=>{
   if(document.documentElement.scrollTop>1400)
   setInterval(callCounters,500)
});


