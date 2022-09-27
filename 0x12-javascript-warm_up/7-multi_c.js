#!/usr/bin/node

const no = parseInt(process.argv[2]);

if (isNaN(no)) {
  console.log('Missing number of occurences');
} else {
  for (let x = 0; x < no; x++) {
    console.log('C is fun');
  }
}
