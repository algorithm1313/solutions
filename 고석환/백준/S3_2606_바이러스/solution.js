const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');

const N = +input[0];
const adj = Array.from({length: N+1}, () => []);

input.slice(2).map(line => line.split(' ').map(Number)).forEach(([from, to]) => {
  adj[from].push(to);
  adj[to].push(from);
})

const dfs = (here, visited = new Set()) => {
  visited.add(here);
  let ret = 0;

  for(let there of adj[here]){
    if(visited.has(there)) continue;
    ret += 1 + dfs(there, visited);
  }
  return ret;
}

const answer = () => {
  return dfs(1);
}

console.log(answer());