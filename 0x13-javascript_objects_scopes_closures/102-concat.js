#!/usr/bin/node
const fs = require('fs');


const A = process.argv[2];
const B = process.argv[3];
const C = process.argv[4];

if (
  fs.existsSync(A) &&
fs.statSync(A).isFile &&
fs.existsSync(B) &&
fs.statSync(B).isFile &&
fileC !== undefined
) {
  const fileOne = fs.readFileSync(A);
  const fileTwo = fs.readFileSync(B);
  const stream = fs.createWriteStream(C);
  stream.write(fileOne);
  stream.write(fileTwo);
  stream.end();
}
