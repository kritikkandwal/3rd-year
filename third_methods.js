let arr = ["pune", "delhi", "mumbai"] ;

arr. forEach((val, idx, arr) => {
console. log (val. toUpperCase(), idx) ;
});


let nums = [67, 52, 39];

let newArr = nums. map ( (val) =>{
return val * val;
});

console.log(newArr);


let arr2 = [1, 2, 3, 4, 3, 6, 7];

let evenArr = arr2. filter( (val) =>{
return val % 2 != 0;
});
console. log (evenArr) ;