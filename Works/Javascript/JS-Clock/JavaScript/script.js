const hour=document.querySelector('#hr');
const minute=document.querySelector('#mn');
const second=document.querySelector('#sc');




setInterval(()=>{
    let date=new Date();
    let hr=date.getHours()*30;
    let mn=date.getMinutes()*6;
    let sc=date.getSeconds()*6;
    hour.style.transform=`rotateZ(${(hr)+ (mn/12)}deg)`;
    minute.style.transform=`rotateZ(${mn}deg)`;
    second.style.transform=`rotateZ(${sc}deg)`;
},1000);