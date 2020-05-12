#!/usr/bin/node
// Array * by index
const oldList = require('./100-data').list;
const newList = oldList.map(function (cur, index) {
  return cur * index;
});

console.log(oldList);
console.log(newList);
