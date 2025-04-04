const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const input = fs.readFileSync('./input.txt').toString().split(' ');

const [A, B, C] = input.map(Number);

const go = (a, b) => {
  if(b <= 1) return a % C;
  let ret = go(a, Math.floor(b/2));
  
  ret = (ret * ret) % C;
  if(b % 2) ret = (ret * a) % C;
  return ret;
}

const answer = (A, B, C) => {
  console.log(A, B, C);

  return go(A, B);
}

// gpt 코드
// function modularExponentiation(a, b, c) {
//   if (b === 0) return 1;
//   let half = modularExponentiation(a, Math.floor(b / 2), c);
//   let result = (half * half) % c;
//   if (b % 2 !== 0) result = (result * a) % c;
//   return result;
// }

console.log(answer(A, B, C));