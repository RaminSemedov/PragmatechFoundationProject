Intepreter & Compiler.

 Hem interpreter hem de compiler high level dillerinde yazilan kodu byte (ikili) koda chevirir.
 Interpreter yazilan kodu setir setir oxuyaraq onu run  edir.Compiler ise kodu butovlukde oxuyaq sonda onu run
 edir.
   Intrepreter ustunlukleri:                                        Compiler ustunlukleri:
   
   Emeliyyat sisteminden asilidi deyil.                              Daha tez ishleme suretine malikdir.                  
   Yaddashdan daha qenaetli shekilde istifade edir.                  Istifadechinin komputerinde compilerin olmasi teleb olunmur
   
   Intrepreter chatishmamazliqlari:                                 Compiler chatishmamazliqlari:
   Proqramin ishlemesi uchun interpreter teleb olunur.              Program emeliyyat sisteminden asilidir.
   Ashagi ishleme sureti.                                           Kodda her hansi bir deyishiklik olunduqda recompiler teleb olunur.
-----------------------------------------------------------------------

// 1.Function declaration ve function assignment arasındakı əsas fərqlər nələrdir?
// Nümunələrlə izah edin

//Function declaration ile teyin olunan funksiya programin istenilen yerinde chagirila biler.
//Function assignment ile   teyin olunan funksiya yalniz teyin olunandan sonra chagirila biler

```

myFunc();
function myFunc(){
    console.log("Function declaration");
}
```


// a deyisheni teyin olunmamishdan once funksiyani chagira bilmrik
// a() -  a is not defined error-u ekrana chixacaq
```
let a=function(){
    console.log("function assignment");
}
```
//Arrow functions  Function declaration ve Function assignment daha sadeleshmish 
//ve qisaldilmish formasidir.Meselen yuxaridaki funksiyani biz
```
a=()=>{
    console.log(" Arrow function");
}
```
 //kimi yaza bilerik.Eger funksiya hech bir parametr yoxdusa biz () bosh saxlayiriq.
  ```
 let b =(x,y)=>{
    return x+y;
}
```
//bir neche parametr teleb olunarsa  onlari () yaziriq.
```
let c=x=>{
    return x++;
}
```
//Bir parametr teleb olunursa () yazmamaq da olar

c=x=>x++; //Eger funksiyanin ishi yalniz deyer qaytarmaqdirsa onda moterizelerden istida etmemek de olar



/*
```
function Foo(){
  let a=5
}

function Bar(){
  console.log(a)
}
```
Yuxarıdakı funksiyalara elə əlavələr edin ki Bar() icra olunduğu zaman ekrana 5 çap olunsun.*/
```
function Foo(){
    let a=5;
    return a;
  }

  function Bar(){
    let a=Foo();
    console.log(a)
  }

  
  var test=5;
  function Foo(){
    var test=2;
    test++;
    console.log(test);
  }
  Foo();
  console.log(test);
  ```
  ------------------------------------------------------------------------------
  --------------------
  arr massivini sort metodu olmadan azdan çoxa sıralayın
 
 
  ```

  let array1=[1,0,7,8,9,23,90,8];

   
   function sort(arr){
  
    for(let i=0;i<arr.length;i++){
        for(let j=i+1;j<arr.length;j++){

            if(arr[i]>arr[j]){
                let temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }

}



console.log(array1); 
sort(array1);
console.log(array1); 

```

