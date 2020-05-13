#!/usr/bin/node
// Copy the bodies

const req = require('request');
const fs = require('fs');

req(process.argv[2], (err, res, body) => {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, 'utf-8', error => {
    if (error) throw error;
  });
});
