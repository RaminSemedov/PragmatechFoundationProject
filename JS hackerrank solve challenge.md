### Task 1 -  hello-world
https://www.hackerrank.com/challenges/js10-hello-world/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}


function greeting(parameterVariable) {
    
    console.log('Hello, World!');
    console.log('Welcome to 10 Days of JavaScript!');
    
}


```

### Task 2- data-types
https://www.hackerrank.com/challenges/js10-data-types

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   The variables 'firstInteger', 'firstDecimal', and 'firstString' are declared for you -- do not modify them.
*   Print three lines:
*   1. The sum of 'firstInteger' and the Number representation of 'secondInteger'.
*   2. The sum of 'firstDecimal' and the Number representation of 'secondDecimal'.
*   3. The concatenation of 'firstString' and 'secondString' ('firstString' must be first).
*
*	Parameter(s):
*   secondInteger - The string representation of an integer.
*   secondDecimal - The string representation of a floating-point number.
*   secondString - A string consisting of one or more space-separated words.
**/
function performOperation(secondInteger, secondDecimal, secondString) {
    // Declare a variable named 'firstInteger' and initialize with integer value 4.
    const firstInteger = 4;
    console.log(firstInteger+Number(secondInteger));
    
    // Declare a variable named 'firstDecimal' and initialize with floating-point value 4.0.
    const firstDecimal = 4.0;
     console.log(firstDecimal+Number(secondDecimal));
    
    // Declare a variable named 'firstString' and initialize with the string "HackerRank".
    const firstString = 'HackerRank ';
    console.log(firstString+String(secondString));
    
    // Write code that uses console.log to print the sum of the 'firstInteger' and 'secondInteger' (converted to a Number        type) on a new line.
    
    
    // Write code that uses console.log to print the sum of 'firstDecimal' and 'secondDecimal' (converted to a Number            type) on a new line.
    
    
    // Write code that uses console.log to print the concatenation of 'firstString' and 'secondString' on a new line. The        variable 'firstString' must be printed first.
    
}


```

### Task 3- arithmetic-operators
https://www.hackerrank.com/challenges/js10-arithmetic-operators/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   Calculate the area of a rectangle.
*
*   length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the rectangle's area.
**/
function getArea(length, width) {
    let area;
    // Write your code here
    area=length*width
    
    return area;
}

/**
*   Calculate the perimeter of a rectangle.
*	
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*   
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;
    // Write your code here
    perimeter=(length+width)*2
    
    return perimeter;
}


```

### Task 4-Function
https://www.hackerrank.com/challenges/js10-function/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}
/*
 * Create the function factorial here
 */
function factorial(n){
let f=1;
for(let i=1;i<=n;i++){
f*=i;
}
return f;
}

```
### ### Task 5- If-Else
https://www.hackerrank.com/challenges/js10-if-else/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {
    let grade;
    // Write your code here
    if(score>25 && score <=30)grade='A';
    else if(score>20 && score <=25)grade='B';
    else if(score>15 && score <=20)grade='C';
    else if(score>10 && score <=15)grade='D';
    else if(score>5 && score <=10)grade='E';
    else if(score>0 && score <=5)grade='F';
    
    return grade;
}
```

### Task 6-Switch
https://www.hackerrank.com/challenges/js10-switch/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    // Write your code here
    switch(s[0]){
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        letter='A';
        break;
        
        case 'b':
        case 'c':
        case 'd':
        case 'f':
        case 'g':
        letter='B';
        break;
        
        case 'h':
        case 'j':
        case 'k':
        case 'l':
        case 'm':
        letter='C';
        break;
        
        case 'n':
        case 'p':
        case 'q':
        case 'r':
        case 't':
        case 's':
        case 'v':
        case 'w':
        case 'x':
        case 'y':
        case 'z':
        letter='D';
        break;
    }
    
    return letter;
}


```

### Task-7 Loops

https://www.hackerrank.com/challenges/js10-loops/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    
    for(let i=0;i<s.length;i++){
        if(s[i]=='a'|| s[i]=='e'|| s[i]=='i'|| s[i]=='o' || s[i]=='u'){
            console.log(s[i]);
        }
    }
    for(let i=0;i<s.length;i++){
    if(s[i]!='a' && s[i]!='e' && s[i]!='i' && s[i]!='o' && s[i]!='u'){
        console.log(s[i]);}
    }
}




```

### Task 8-Arrays

https://www.hackerrank.com/challenges/js10-arrays/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    nums.sort((a,b)=>b-a);
    for(let i=1;i<nums.length;i++){
         if(nums[i]<nums[i-1] && nums[i]>nums[i+1])
         return nums[i]
    }
    
}



```

### Task-9-Create a Rectangle Object
https://www.hackerrank.com/challenges/js10-objects/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    return {
        length:a,
        width:b,
        perimeter:2*(a+b),
        area:a*b
    }
}



```





### Task-10 - Count Objects

https://www.hackerrank.com/challenges/js10-count-objects/problem

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
let sum=0;
    for(let i=0;i<objects.length;i++){
       if( objects[i].x==objects[i].y)
       sum++;
    }
    return sum;
    
}




```

### Task-11 Let and Const
https://www.hackerrank.com/challenges/js10-let-and-const/problem?isFullScreen=false

```
'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim()
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    
    let r=2.6; 
      
 
    const PI=Math.PI;
    // Print the area of the circle:
    let area=PI*(r*r);
      console.log(area);
    
    // Print the perimeter of the circle:
    let perimeter=2*PI*r
      console.log(perimeter)
    try {    
```
### Task-12 Classes
https://www.hackerrank.com/challenges/js10-class/problem?isFullScreen=false

```
/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
class Polygon{
     sides=[];
    constructor(sideLength){
         for(let i=0;i<sideLength.length;i++){
             this.sides[i]=sideLength[i];
         }       
    }
    perimeter=function(){
      let sum=0;
      for(let i=0;i<this.sides.length;i++){
          sum+=this.sides[i];
      }
      return sum;
    }
}


```

### Task-13 Inheritance

```
class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}

/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */

Rectangle.prototype.area=function(){
    return this.w*this.h;
}

/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */
class Square extends Rectangle{
    
       constructor(w){
       super(w);
       this.h=w;
    }      
}



```

### Task-14 Create a Button 
https://www.hackerrank.com/challenges/js10-buttons-container

```
<!-- HTML -->

<!-- Enter your HTML code here -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
         <link rel="stylesheet" href="css/button.css" type="text/css">
        <title>Button</title>
    </head>
    <body>
        <button id='btn'>0</button>
        <script src="js/button.js" type="text/javascript"></script>
    </body>
</html>
```

```
<!-- CSS -->

#btn{
    width:96px;
    height:48px;
    font-size:24px;
}
```
```
<!-- JS -->

  let btn=document.querySelector('#btn');
  let counter=0; 

 btn.addEventListener('click',()=>{
    
        btn.innerHTML=++counter;
   
 })
```

### Task-15