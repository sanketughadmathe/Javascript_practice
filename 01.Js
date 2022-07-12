// const prompt = require('prompt-sync')();
const prompt = require('prompt-sync')();

if (typeof window !== 'undefined') {
  // alert("Thanks for using the Web App! Please refresh the page to start over.")
  // 👉️ can use alert()
} else {
  // console.log('You are on the server')
  // 👉️ can't use alert()
} 

// function addUpTo(n) {
//   let total = 0;
//   for (let i = 0; i < n; i++) {
//     total += n;
//   }
//   return total
// }
  
function addUpTo(n) {
  return n * (n+1) / 2;
}

var t1 = performance.now()
addUpTo(10000000000)

var t2 = performance.now()
console.log(`Time Elapsed: ${(t2 -t1)/100} seconds`)