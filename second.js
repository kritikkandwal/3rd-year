// Arrow function 

const arrowSum=(a,b)=>{
    console.log(a+b);
}

function vowel(sent){
    let c = 0; // counter
    sent = sent.toLowerCase(); 
    for(let i=0;i<sent.length;i++){
        if(sent[i]=='a' || sent[i]=='e' || sent[i]=='i' || sent[i]=='o' || sent[i]=='u'){
            c++
        }
    }
    return c;
}

console.log(vowel("Hey this side Kritik"));

arrowSum(3,4);