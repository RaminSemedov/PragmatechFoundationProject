const container=document.querySelector('.container');

function createBoxes(boxSayi,sutunSayi,boxHundurluyu,araMefase){

  let boxes=[];

    for(let i=0;i<boxSayi;i++){
        boxes[i]=document.createElement('div');
        boxes[i].style.height=boxHundurluyu+'px';
        boxes[i].style.width=boxHundurluyu+'px';
        boxes[i].style.margin=araMefase+'px';
        boxes[i].className='box';
        container.appendChild(boxes[i]);       
    }
         container.style.gridTemplateColumns=getColumns(sutunSayi);
       
    
    
         function getColumns(sutunSayi){
             let s='';
             for(let i=0;i<sutunSayi;i++){
              s+='1fr ';
             }
            return s;
         }
}
createBoxes(20,2,50,5);
