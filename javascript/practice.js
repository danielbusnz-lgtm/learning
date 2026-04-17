/*
JavaScript Practice — 10 Questions
====================================
Run with:  node practice.js

Each question has a "// your code here" slot.
Use console.log(...) to check your answers.
*/

const { useState } = require("react");


// --- 1. VARIABLES (let vs const) ---
//


// Declare a variable `age` set to 23 that CAN be reassigned later.
// Declare a variable `name` set to "Dan" that CANNOT be reassigned.
// Reassign age to 24. Print both.
//
// your code here


// --- 2. ARROW FUNCTIONS ---
// Write an arrow function `square` that takes a number and returns its square.
// Call it with 7. Print the result.

// your code here

function add(a, b) {
    return a + b;
}





// --- 3. ARRAYS + .map ---
// Given the array below, use .map to return a new array where every
// number is multiplied by 3. Print the result.
const nums = [1, 2, 3, 4, 5];
// your code here
//


const array = nums.map(n => n * 3);
console.log(array)

// --- 4. ARRAYS + .filter ---
// Using the same `nums` array above, use .filter to keep only even numbers.
// Print the result.
//
// your code here

const evens = nums.filter(n => n % 2 === 0)


// --- 5. OBJECTS + DESTRUCTURING ---
// Given the user object below, destructure `name` and `age` into their own
// variables and print them.
const user = { name: "Alice", age: 30, city: "Seattle" };
// your code here
const { name, age1, city } = user;
console.log(name, age1, city);

// --- 6. CLASSES ---
// Create a class `Dog` with a constructor that takes `name` and `breed`.
// Add a method `bark()` that returns "<name> says woof!".
// Create a new Dog with name "Rex" and breed "Husky". Print the bark.
//
// your code here
class Dog {
    constructor(name, bread) {
        this.bread = bread;
        this.name = name;
    }
    bark() {
        return this.name + ' says woof!';
    }
}
const MyDog = new Dog('Rex', 'Labrador');
console.log(MyDog.bark());

// --- 7. CONDITIONALS + TERNARY ---
// Given `age = 17`, use a ternary to assign a variable `label` that's
// "adult" if age >= 18, else "minor". Print it.
const age = 17;
// your code here
const label = age >= 18 ? 'adult' : 'minor';
console.log(label);



// --- 8. LOOPS (for...of) ---
// Given the array below, loop over it and print each name on its own line.
const names = ["Dan", "Bob", "Charlie"];
// your code here

for (const name of names) {
    console.log(name);
}



// --- 9. TRUTHY / FALSY ---
// Given the values below, print whether each one is truthy or falsy
// (hint: use an if/else or ternary).
const values = [0, "", "hello", null, [], 42];
// your code here


for (const value of values) {
    if (value) {
        console.log(value, 'is truthy');
    }
    else {
        console.log(value, 'is falsy');
    }
}

// --- 10. ASYNC / AWAIT + try/catch ---
// Write an async function `getJoke` that:
//   - fetches from "https://icanhazdadjoke.com/" with header { Accept: "application/json" }
//   - parses the JSON
//   - returns data.joke
//   - wraps in try/catch and logs "failed" on error
// Call it and print the joke.
//
// your code her
//
//
//

async function fetchData() {
    try {
        const response = await fetch('https//example.com');
        const data
    }
}

function Counter() {
    const [count, setCount] = useState(0);

    return (
        <button

    )
}
