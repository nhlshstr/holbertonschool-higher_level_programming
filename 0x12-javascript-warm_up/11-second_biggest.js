#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length === (1 || 0)) return 0;
  let max = -Infinity;
  let max2 = -Infinity;
  for (let x = 0; x < arr.length; x++) {
    if (arr[x] > max) {
      max2 = max;
      max = arr[x];
    } else if (max > arr[x] > max2) {
      max2 = arr[x];
    }
  }
  return max2;
}

const arr = process.argv.slice(2, process.argv.length).map(Number);
console.log(secondBiggest(arr));
