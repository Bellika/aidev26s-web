// Variable
let firstName = "John";

// Function
function printName(name) {
    console.log(`My name is ${name}`);
}

printName(firstName);


console.log('############# Object intro ############');
let house = {
    // Properties
    color: 'red', 
    windows: 4, 
    area: 400,

    //Methods
    description: function() {
        return `This is a ${this.color} house with ${this.windows} windows`;
    }
}

console.log(house);
// The properties of the object
console.log(house.color);
console.log(house.windows);
console.log(house.area);
// May also call the properties in a way, similar to an arrays
console.log(house['color']);
console.log(house['area']);
console.log(`This is a ${house.color} house with ${house.windows} windows`);


// The methods of the object
console.log(house.description());


// The benefits of coding like this
let houseB = Object.create(house);
houseB.color = "Yellow";
houseB.windows = "20";
houseB.area = "800";
console.log(houseB.description());

let houseC = Object.create(house);
houseC.color = "Purple";
houseC.windows = "10";
houseC.area = "600";
console.log(houseC.description());

console.log('############# Object with init(), a function similar to a construct ############');
let person = {
    // Properties
    firstName: 'John', 
    lastName: "Doe", 
    age: 35,
    
    // Methods
    init: function(firstName, lastName, age) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    },

    fullName: function() {
        return this.firstName + " " + this.lastName;
    },

    greeting: function() {
        return "Hello! My name is " + this.fullName();
    }
}


let natalia = Object.create(person);
natalia.init("Natalia", "Sundström", "24")
console.log(natalia.greeting());


let richard = Object.create(person);
richard.init("Richard", "Chimama", "27");
console.log(richard.greeting());


console.log('############# Object constructors ############');
function PersonBlueprint(first, last, age) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;

    this.fullName = function() {
        return this.firstName + " " + this.lastName;
    }

    this.greeting = function() {
        return "Hello! My name is " + this.fullName();
    }
}

let radovan = new PersonBlueprint('Radovan', 'Scekic', 35);
console.log(radovan.greeting());


console.log('############# Classes  ############');

class Animal {
    constructor(name, sound, favoriteFood) {
        this.name         = name;
        this.sound        = sound;
        this.favoriteFood = favoriteFood;
    }

    getFrase() {
        return `My name is ${this.name} and I like to eat ${this.favoriteFood}, ${this.sound}!`;
    }
}

let mouse = new Animal('Micky', 'piip piip', 'cheese');
console.log(mouse.getFrase());

let lion = new Animal('Simba', 'AAAAAARRRRHHHH', 'YOU');
console.log(lion.getFrase());



console.log('############# About built-in objects nad functions ############');

console.log([1, 2, 3].length);     // property of Array
console.log([1, 2, 3].push(4));    // method of Array
console.log("string".length);      // property of String
console.log("string".slice(-1));   // method of String
console.log((123).toString());     // method of Number
console.log(new Date().getFullYear()) // Creates a new object and uses the method getFullYear
console.log(Math.PI)               // Property


// In JavaScript, objects are king. If you understand objects, you understand JavaScript.




// When to use a Class/blueprint and when to use an object right away

// When the need to work with multiple examples av the same object accours, then a blueprint/class is more appropiate
console.log(new Date().getFullYear());


// When working with only ONE object, then no need to create a blueprint/class. May create the object straight away.
console.log(Math.PI)               // Property
