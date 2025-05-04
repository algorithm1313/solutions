const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(e => Number(e));

const go = (idx, arr, input) => {
    if(idx > 9) return;
    if(arr.length === 7){
        let sum = 0;
        // arr.map(e => sum += e);
        sum = arr.reduce((acc, cur) => cur += acc);
        
        if(sum === 100){
            arr.map(e => console.log(e));
        }

        return;
    }
    
    arr.push(input[idx]);
    go(idx + 1, arr, input);
    arr.pop();

    go(idx + 1, arr, input);

    return;
}

const answer = (input) => {
    const arr = [];
    go(0, arr, input)
}

answer(input)