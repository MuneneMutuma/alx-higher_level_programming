#!/usr/bin/node

const arr = [];

for (let x = 2; x < process.argv.length; x++) {
  arr.push(parseInt(process.argv[x]));
}

arr.sort((a, b) => b - a);

if (arr.length < 2) {
  console.log(0);
} else {
  console.log(arr[1]);
}
