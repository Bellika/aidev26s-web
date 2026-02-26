/**
 * 
 * Functions
 */

console.log('############# Different function declarations ################');
dummyFunction(); // invoking the function
dummyFunction(); // invoking the function
dummyFunction(); // invoking the function


// Declaring function in standard way
// This way of declaring a function allows usage before declaration
// Javascript moves this kind of function declaration  to the top of the script
// This procedure is called hoisting
function dummyFunction() {
    console.log("Function declared in standard way");
}


// Function expression
// Must be declared before usage
let dummyFunction2 = function() {
    console.log("Function declared with function expression");
}
dummyFunction2(); // invoking the function


// Arrow functions
// Must be declared before usage
let dummyFunction3 = () => {
    console.log("Function declared with arrow functions");
}
dummyFunction3();


//Automatically (self-invoking) and anonymous function
(function() {
    console.log('Self invoking and anonymous function')
})();



console.log('############# Functions with parameters and return-statement ################');

// Limited function without parameters and return-statement
function calculateArea() {
    let height = 5;
    let width = 4;
    let area = height * width;

    console.log(`Rectangle area is: ${area}`);
}

calculateArea();


// Function made more flexible with parameters and return
function calculateArea2(height, width) {
    let area = height * width;
    
    console.log('%cInside of the calculateArea2 function. BEFORE return', 'color: red');
    return area; // Returns the value, and jumps out of the function. No more code execusion in the function, after return-statement 
    console.log("Inside of the calculateArea2 function. AFTER return") // Will never run
}

let squearArea = calculateArea2(10, 10);
console.log(`Square area is: ${squearArea}`);
let rectangleArea = calculateArea2(3, 7);
console.log(`Rectangle area is: ${rectangleArea}`);
let triangleArea = calculateArea2(3, 7) / 2;
console.log(`Triangle area is: ${triangleArea}`);


// Rewrite  the calculateArea2 function with Arrow functions
// let calculateArea3 = (height, width) => {
//     return height * width;
// }
let calculateArea3 = (height, width) => height * width;

squearArea = calculateArea3(10, 10);
console.log(`Square area is: ${squearArea}`);
rectangleArea = calculateArea3(3, 7);
console.log(`Rectangle area is: ${rectangleArea}`);
triangleArea = calculateArea3(3, 7) / 2;
console.log(`Triangle area is: ${triangleArea}`);


console.log('############# Scopes ################');

let globalS = 5; // Global scope
function functionScope() {
    let functionS = 4; // Functions scope
    
}
functionScope();
console.log(globalS); 
// console.log(functionS);  // Cant use a function scope defined variable, outside the function


console.log('############# Block-scopes: let VS var ################');

var x = 5; // Global scope
for (var x = 1; x < 10; x++) { //Block scope
}
console.log(x) // 10


let y = 5; // Global scope
for (let y = 1; y < 10; y++) { //Block scope
}
console.log(y) // 5


console.log('############# const ################');

// const variables are as the name implies, its a constant, meaning not allowed to change value or redeclare 
const PI = 3.14;
//PI = 2 // Not allowed
