// JavaScript allows us to work with primitives (strings, numbers, etc.) as if they were objects.
//https://javascript.info/primitives-methods
//https://javascript.info/rest-parameters-spread

// using spread operator
function sumAll(...args) {
    let sum = 0;

    for (let arg of args) {
        sum += arg
    }
    return sum
}
console.log(sumAll(1, 2))
console.log(sumAll(1, 2, 3, 4))
console.log(sumAll(1, 2, 3, 4, 10, 13))

// another example

function showName (firstName, lastName, ...title) {
    return title[0] + " " + firstName + " " + lastName
}
// the spread operator helps in tackling 
console.log(showName("Pratyush", "Gupta", "Major", "General", "Janitor", "Data Cleaner", " "))