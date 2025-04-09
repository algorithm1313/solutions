const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// const input = fs.readFileSync('./input.txt').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const map = input.slice(1).map(a => a.split('').map(Number))

const dir = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1]
];

const visited = Array.from({length: n}, () => Array(m).fill(0));

const answer = (n, m, map) => {
  visited[0][0] = 1;
  const queue = [];
  
  queue.push([0, 0]);

  while(queue.length > 0){
    const [y, x] = queue.shift();

    for (const [dy, dx] of dir){
      const [ny, nx] = [y + dy, x + dx];

      if(ny < 0 || nx < 0 || ny >= n || nx >= m) continue;
      if(visited[ny][nx] || map[ny][nx] === 0) continue;

      visited[ny][nx] = visited[y][x] + 1;
      queue.push([ny, nx]);
    }

  }

  return visited[n-1][m-1];
}

console.log(answer(n, m, map));