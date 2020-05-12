#!/usr/bin/node
// Reads & prints file

const fs = require('fs');

fs.readFile('cisfun', 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
