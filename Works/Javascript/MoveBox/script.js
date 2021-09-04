let btn=document.querySelector('.btn');
let box=document.querySelector('.box');
let body=document.querySelector('body');


btn.style.left=document.documentElement.clientWidth/2-btn.clientWidth/2+'px';
btn.style.top=document.documentElement.clientHeight/2-btn.clientHeight/2+'px';


let x=0;
let y=0;




btn.addEventListener('click',()=>{

    let interval1=setInterval(()=>{        
        if(box.getBoundingClientRect().right!=window.innerWidth){
        box.style.transform=`translate(${x++}px)`;   }      
        else{
             clearInterval(interval1); 
             let interval2=setInterval(()=>{  
                if(box.getBoundingClientRect().bottom!=document.documentElement.clientHeight){
                    box.style.top=`${y++}px`;
                }
                else{
                    clearInterval(interval2);
                }
    
            } ,1 )
            

        }},1)

        

       

       
         
         
          
        
      






})


