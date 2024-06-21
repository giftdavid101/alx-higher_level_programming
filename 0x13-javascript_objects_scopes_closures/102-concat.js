#!/usr/bin/node
const fs = require('fs');

if (
  fs.existsSync(process.argv[2]) &&
fs.statSync(process.argv[2]).isFile &&
fs.existsSync(process.argv[3]) &&
fs.statSync(process.argv[3]).isFile &&
fileC !== undefined
) {
  const fileOne = fs.readFileSync(process.argv[2]);
  const fileTwo = fs.readFileSync(process.argv[3]);
  const stream = fs.createWriteStream(process.argv[4]);
  stream.write(fileOne);
  stream.write(fileTwo);
  stream.end();
}
