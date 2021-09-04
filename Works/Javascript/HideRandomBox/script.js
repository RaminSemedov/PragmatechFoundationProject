let boxes=document.querySelectorAll('.box');
let container=document.querySelector('.container');
let counter=boxes.length;

let numbers=[];
for(let i=0;i<boxes.length;i++){
    numbers[i]=i;
}

for(let i=0;i<boxes.length;i++){
    boxes[i].addEventListener('click',()=>{
        let random=Math.floor(Math.random()*counter);
        boxes[numbers[random]].style.visibility='hidden' ;
        numbers.splice(random,1);
        counter--;
        console.log(counter);
   })
   
}

container.addEventListener('click',(e)=>{
    if(e.target.className=='container' && counter==0){
    for(let i=0;i<boxes.length;i++){        
            boxes[i].style.visibility='visible';
            counter=10;
            numbers=[0,1,2,3,4,5,6,7,8,9];        
    }
}
})