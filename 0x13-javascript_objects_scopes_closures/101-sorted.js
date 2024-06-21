#!/usr/bin/node

const { dict } = require('./101-data.js');
const hashT = {};
for (const i in dict) {
    if (hashT[dict[i]] === undefined) {
	hashT[dict[i]] = [];
    }
    hashT[dict[i]].push(i);
}
console.log(hashT);
