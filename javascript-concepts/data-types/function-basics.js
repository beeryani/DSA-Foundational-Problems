// In JS, functions are objects
//https://javascript.info/closure#tasks

// Task #1

let name = "John"

sayHi = () => {
    console.log("Hi " + name)
}

name = "Pete"
sayHi();
// The function takes the latest assignment of the name variable when being called

// Task #2

makeWonder = () => {
    let naam = "Cutie"
    return () => {
        console.log(naam)
    }
}

let naam = "John"

let work = makeWonder();

work();

// the output will be "Cutie" because the work() returns an arrow function for which the local variable is "Cutie", in case we had returned a variable then, 
//work() would have picked the latest value of the "naam"

//Task #3

function makeCounter () {
    let count = 0;
    return () =>{
        return count++;
    }
}

let counter = makeCounter();
let counter2 = makeCounter();

console.log(counter()) //0
console.log(counter()) //1

console.log(counter2()) //0
console.log(counter2()) //1

// each function is a different invocation of the makeCounter function

//Task #4

// Constructor Function
function Counter() {
    let count = 0;

    this.up = () => {
        return ++count;
    };

    this.down = () =>  {
        return --count;
    };

    this.show = () =>{
        return count;
    }
}

let counterOne = new Counter();

console.log("This is the current value of " + counterOne.show())
console.log(counterOne.down());
console.log(counterOne.down());

// Task #5 

let phrase = "Hello";

if (true) {
    let user = "Supremacy";
    function sayHenlo(){
        console.log(`${user} hue hue ${phrase}`)
    }
}

sayHenlo();

// Task #6: get back to this later

// Task #7 

// let x = 1;

// function func() {
//     console.log(x)

//     let x = 2;
// }

// func();

// Standard Properties of Function object 

//Counter property

function namaste() {
    console.log("Adaab")
    namaste.counter++
}

namaste.counter = 0;

namaste();
namaste();

console.log(`${namaste.counter}`)


//https://javascript.info/function-object
 /* 
 Difference b/w Function Expression and Function Declaration
 */

 //Closure
 /* 
 A function bundled with it's lexical scope is refered to as closure. Follow the example below:
 */

 function x() {
     var a = 7;
     function y() {
         console.log(a)
     }
     return y;
 }

 let z = x();
z(); // the return value of x() i.e. y() is stored in z, when z is called, it is referring to y but y needs 'a' to return value.
/* 
Here the concept of Closure kicks in. No matter where the function is being called, it will carry its lexical environment.
For example, in our case, a was not reference in the global env but only within x, but y carried its lexical env, hence it could access it.
*/
console.log(x());
