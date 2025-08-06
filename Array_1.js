// const prompt = require("prompt-sync")();
let size = parseInt(prompt("Enter the size of the array:"));  // Assume the size of the array is 5
let arr = [];

for (let i = 0; i < size; i++) {
    let element = parseInt(prompt("Enter element " + (i + 1) + ":"));
    arr.push(element);  // Adds the element to the array
}
console.log("The array is:", arr);


//using pop
arr.pop();     // Removes 5 from the end
console.log(arr);


//using shift and unshift
arr.unshift(0);  // Adds 0 at the start
arr.shift();     // Removes 0 from the start
console.log(arr);

