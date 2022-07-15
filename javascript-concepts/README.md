# Concepts studied on 20220706
## Important concepts from various tutorials and lectures

### Main Source:
1. Akshay Saini JS lectures (https://www.youtube.com/c/akshaymarch7)
2. javascript.info (https://javascript.info/)

## Concept 1 : Scope Chain and Lexical Environment

Need to understand Block Scope before adding it here.
Recommended Reading (https://javascript.info/closure)

## Concept 2 : Temporal Dead Zone

In JS, let and const variable type are scriter in terms of declaration.
var keyword is hoisted and is initialized as `undefined`
const and let keyword are also hoisted but they are not initialized until referenced/called. This leads to the 
generation of `temporal dead zone` which leads to error in case let or const variables are called before initialisation.

## Concept 3 : First Class Function
### important subtopics
* Function Statement
* Function Expression v/s Function Declaration
* Anonymous Functions
* Prelude to Arrow Functions
* Difference between Parameters and Arguments

## Concept 4 : Closures

Recommended Reading (https://javascript.info/closure)

---

# Concepts studied on 20220707
## Important concepts from various tutorials and lectures

## Concept 1 : Callback Functions

Main takeaways on how to use Closures to hide variables from the global scope to avoid any interference while dealing with a larger code base.

## Concept 2 : Event Loops

## Concept 3 : Block Scope