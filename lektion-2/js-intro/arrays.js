/**
 * Arrays
 */

let myArray = [
  1,                      // Index 0
  2,                      // Index 1
  3,                      // Index 2
  'four',                // Index 3        
  'five',                 // Index 4        
  false,                  // Index 5    
  true,                   // Index 6    
  [                       // Index 7
      'nested array',
      23
  ]
];

// Display array element
console.log(myArray[0]); // 1
console.log(myArray[1]); // 2
console.log(myArray[2]); // 3
console.log(myArray[3]); // "four"
console.log(myArray[4]); // "five"
console.log(myArray[5]); // false
console.log(myArray[6]); // true

// Nested arrays
console.log(myArray[7]); // ['nested array', 23]
console.log(myArray[7][0]); // 'nested array'
console.log(myArray[7][1]); // 23

// Update a specific array element
myArray[4] = 5;
console.log(myArray[4]); // 5

console.log(myArray)
console.log(myArray.length) // 8


// Array is very similar to how strings are treaded. With tools such as .length, .charAt()
let string = "Hello";
console.log(string.length);
console.log(string.charAt(0));




/**
* Array loops
*/

console.log("######### Arrays with different loops #############");

console.log("********** Standard for-loop **********");
// console.log(myArray.length) // 8
for (let i = 0; i < myArray.length; i++) {
  console.log(`Array index is ${i}`);
  console.log(myArray[i]);    
  // myArray[0]
  // myArray[1]
  // myArray[2]
  // myArray[3]
  // myArray[4]
  // myArray[5]
  // myArray[6]
  // myArray[7]
}


// Used for both displaying and manipulalting the array elements
console.log("**********  for/in-loop **********");
for (let i in myArray) {
  console.log(`Array index is ${i}`);
  console.log(myArray[i]);  
  // myArray[i] += ' - updated';
  // console.log(myArray[i]);  
}
// Example on an array that begins with inex 1, instead of 0
let myArray2 = [];
myArray2[1] = 'Hej';
myArray2[2] = 'Då';
for (let i in myArray2) {
  console.log(`Array index is ${i}`);
  console.log(myArray[i]);  
}

// Used for Only displaying the array elements
console.log("**********  for/of-loop **********");
for (let value of myArray) {
  console.log(value); 
}

// Used for Only displaying the array elements
console.log("**********  array loop with built-in function .forEach() **********");
myArray.forEach(function(value, index, array) {
  console.log(`value: ${value}`);
  console.log(`Index: ${index}`);
  console.log(`Array: ${array}`);
});

// Rewrite the above with arrow functions
// myArray.forEach((value, index, array) => {
//     console.log(`value: ${value}`);
//     console.log(`Index: ${index}`);
//     console.log(`Array: ${array}`);
// });



/**
* Array functions
*/

console.log("######## Array functions ###########")
let numbers = [1, 3, 5, 7, 9];


console.log(numbers);
// Lets multiply all elements by 10

// Solution 1
// for (let i in numbers) {
//     numbers[i] *= 10;
// }
// console.log(numbers);


// Solution 2 with array function .map()
// let result = numbers.map(function(value, index, array) {
//     return value * 10
// })
// console.log(result);

// Solution 3 with array function .map() AND arrow functions
let result = numbers.map((value) => value * 10);
console.log(result);



// Concatenate all elements to a string, seperated by space
let words = ['Hello', 'World', 'Wide', 'Web'];

// Solution 1
// string = "";
// words.forEach(function(value) {
//     string += value + ' ';
// })

// console.log(string.slice(0, -1));

// Solution 2
console.log(words.join(' '));



/**
* Nested arrays
*/

console.log("############ Nested arrays ############");
// let vehicles = [
//     'Volvo',
//     'Ferrari',
//     'Maserati',
//     'Fiat'
// ];

// let vehiclesStock = [
//     13,
//     2,
//     3,
//     100
// ];

// let vehiclesSold = [
//     1,
//     1,
//     2,
//     50
// ];

let vehicleData = [
  ['Volvo', 13, 1],
  ['Ferrari', 2, 1],
  ['Maserati', 3, 2],
  ['Fiat', 100, 50],
]

console.log(`${vehicleData[0][0]} has sold ${vehicleData[0][1]}, and has only ${vehicleData[0][2]} examples left`);
console.table(vehicleData[0]);
console.table(vehicleData[1]);
console.table(vehicleData[2]);
console.table(vehicleData);


let vehicleDataHTMLList = '';
for (let i1 in vehicleData) {
  vehicleDataHTMLList += '<h4>Vehicle data for ' + vehicleData[i1][0] + '</h4>';
  vehicleDataHTMLList += '<ul>';
  
  for (let i2 in vehicleData[i1]) {
      vehicleDataHTMLList += '<li>' + vehicleData[i1][i2] + '</li>';
  }

  vehicleDataHTMLList += '</ul>';
}
document.getElementById('vehicle-data').innerHTML = vehicleDataHTMLList;
