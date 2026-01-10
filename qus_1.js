const prompt = require("prompt-sync")();
let size=parseInt(prompt("enter size of array"));
let arr=[];

for(let i=0;i<size;i++){
    let element=parseInt(prompt());
    arr.push(element);
}


for(let i=0;i<size;i++){
    arr[i]=arr[i]-arr[i]*0.1;
}

console.log("Discounted prices:", arr);