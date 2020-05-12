#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');

const data = process.argv[3];
const file = process.argv[2];

fs.writeFile(file, data, (err) => {
  if (err) throw err;
});
