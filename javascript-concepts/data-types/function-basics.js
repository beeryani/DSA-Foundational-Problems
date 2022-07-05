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
        return count++;
    };

    this.down = () =>  {
        return count--;
    };

    this.show = () =>{
        return count;
    }
}

let counterOne = new Counter();

console.log("This is the current value of " + counterOne.show())
console.log(counterOne.up());
console.log(counterOne.up());
console.log(counterOne.down());
console.log(counterOne.down());