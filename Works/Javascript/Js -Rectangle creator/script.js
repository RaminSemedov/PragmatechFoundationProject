let btn=document.querySelector('a');
let cont=document.querySelector('.container');
let height=150;
let width=200;
let margin=10;


//Button click effect
btn.addEventListener('mousedown',()=>{
    btn.style.boxShadow='none';
})
btn.addEventListener('mouseup',()=>{
    btn.style.boxShadow='0 10px 10px rgba(0,0,0,.5)';
})


//Button click 
btn.addEventListener('click',()=>{
    //Random colors
let red=Math.floor(Math.random()*255);
let green=Math.floor(Math.random()*255);
let blue=Math.floor(Math.random()*255);
    //Reset box parameters
if(cont.childElementCount==0){
     height=150;
     width=200;
     margin=10;
}

//Create  box
let box=document.createElement('div');
box.style.boxShadow='0 10px 10px rgba(0,0,0,.5)';
box.style.width=width+'px';
box.style.height=height+'px';
box.style.margin='10px';
box.style.marginRight=`${margin}px`;
box.style.borderRadius='10px';
box.style.backgroundColor=`rgb(${red}, ${green}, ${blue})`;
cont.appendChild(box);

//Increment parameters
width+=20;
height+=20;
margin+=5;
})

//Remove boxes
cont.addEventListener('click',(e)=>{
if(e.target.className!='container')
e.target.remove();
})