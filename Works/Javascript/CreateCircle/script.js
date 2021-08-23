let box=document.querySelector('body');
box.addEventListener('click',createCircle);


function getColor(){
    let r=Math.floor(Math.random()*255);
    let g=Math.floor(Math.random()*255);
    let b=Math.floor(Math.random()*255);
    return `rgb(${r},${g},${b})`;
}


function createCircle(e){
let randomSize=Math.floor(Math.random()*200);
let innerBox=document.createElement('div');
innerBox.style.width=randomSize+'px';
innerBox.style.height=randomSize+'px';
innerBox.style.backgroundColor=getColor();
innerBox.className='innerBox';
innerBox.style.left=e.clientX-randomSize/2+'px' ;
innerBox.style.top=e.clientY-randomSize/2+'px';
box.appendChild(innerBox);
box.style.backgroundColor=getColor();
let h=innerBox.getBoundingClientRect().top;
let up=innerHeight-innerBox.getBoundingClientRect().height;
setInterval(()=>{
    
    
    innerBox.style.top=`${h++}px`
    if(innerBox.getBoundingClientRect().bottom>=window.innerHeight){
           h--;
           if(innerBox.getBoundingClientRect().top==0){
               up++;
            }
            else{
               innerBox.style.top=`${up--}px`;
           }
        
}




    

   
   
   
  },)

}




