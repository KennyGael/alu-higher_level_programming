#!/usr/bin/node
const num = process.argv[2];
if (num === undefined) {
  console.log('Missing size');
} else {
  const numInt = parseInt(num);
  if (isNaN(numInt)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < num; i++) {
      let row = '';
      for (let j = 0; j < num; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
