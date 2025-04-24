const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const s = input[0];

const answer = (s) => {
  let ret = "";
  
  for (let i=0; i<s.length; i++){
    let asc = s[i].charCodeAt();
    
    if((asc >= 65 && asc <= 90)){
      // 대문자
      ret += String.fromCharCode((asc - 65 + 13) % 26 + 65);
    }else if (asc >= 97 && asc <= 122){
      // 소문자
      ret += String.fromCharCode((asc - 97 + 13) % 26 + 97);
    }else {
      ret += s[i];
    }
  }
  return ret;
}
process.stdout.write(answer(s));