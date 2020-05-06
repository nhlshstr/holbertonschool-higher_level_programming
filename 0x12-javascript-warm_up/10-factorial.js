#!/usr/bin/node

function fact (num) {
  if (isNaN(num) || num === (1 || 0)) {
    return 1;
  }

  return num * fact(num - 1);
}

console.log(fact(Number(process.argv[2])));
