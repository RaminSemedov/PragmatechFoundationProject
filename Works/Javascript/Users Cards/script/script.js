const container=document.querySelector('.container');
let body=document.querySelector('body');
let users=[
    {
      id:1,
      ad:'Nofel',
      soyad:'Salahov',
    },
    
    {
      id:2,
      ad:'Ramin',
      soyad:'Semedov'
    },
    {
      id:3,
      ad:'Nijat',
      soyad:'Bagirov'
    },
    {
      id:4,
      ad:'Ferid',
      soyad:'Piriyev'
    },
    {
      id:5,
      ad:'Elnar',
      soyad:'Memmedov'
    },
  
   
    
  ]

  function createTeamContainer(param){
      for(let i=0;i<param.length;i++){
            container.appendChild(createBox(param[i]));
      }

}

createTeamContainer(users);




  function createBox(obj){
    let box=document.createElement('div');
    let id=document.createElement('h1')
    id.innerHTML=obj.id;
    let name=document.createElement('h2');
    name.innerHTML=obj.ad
    let surname=document.createElement('h2');
    surname.innerHTML=obj.soyad;
    box.className='box';
    box.appendChild(id);
    box.appendChild(name);
    box.appendChild(surname);

    return box;  

}  

