#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const str = [];
  for (let y = 0; y < size; y++) {
    str.push('X');
  }
  for (let x = 0; x < size; x++) {
    console.log(str.join(''));
  }
}
