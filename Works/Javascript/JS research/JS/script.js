
// 1.Function declaration ve function assignment arasındakı əsas fərqlər nələrdir?
// Nümunələrlə izah edin

//Function declaration ile teyin olunan funksiya programin istenilen yerinde chagirila biler.
//Function assignment ile   teyin olunan funksiya yalniz teyin olunandan sonra chagirila biler



myFunc();
function myFunc(){
    console.log("Function declar");
}



// a deyisheni teyin olunmamishdan once funksiyani chagira bilmrik
// a() -  a is not defined error-u ekrana chixacaq
let a=function(){
    console.log("function assignment");
}

//Arrow functions  Function declaration ve Function assignment daha sadeleshmish 
//ve qisaldilmish formasidir.Meselen yuxaridaki funksiyani biz

a=()=>{
    console.log(" Arrow function");
}
 //kimi yaza bilerik.Eger funksiya hech bir parametr yoxdusa biz () bosh saxlayiriq.
  
 let b =(x,y)=>{
    return x+y;
}
//bir neche parametr teleb olunarsa  onlari () yaziriq.
let c=x=>{
    return x++;
}
//Bir parametr teleb olunursa () yazmamaq da olar

c=x=>x++; //Eger funksiyanin ishi yalniz deyer qaytarmaqdirsa onda moterizelerden istida etmemek de olar



/*
function Foo(){
  let a=5
}

function Bar(){
  console.log(a)
}

Yuxarıdakı funksiyalara elə əlavələr edin ki Bar() icra olunduğu zaman ekrana 5 çap olunsun.*/

function Foo(){
    let a=5;
    return a;
  }

  function Bar(){
    let a=Foo();
    console.log(a)
  }


