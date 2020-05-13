#!/usr/bin/node
// Copy body

const req = require('request');
const fs = require('fs');

req(process.argv[2], (err, res, body) => {
  if (err) throw err;
  fs.writeFile('loripsum', body, 'utf-8', error => {
    if (error) throw error;
  });
});
