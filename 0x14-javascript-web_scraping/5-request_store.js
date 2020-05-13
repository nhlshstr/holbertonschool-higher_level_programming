#!/usr/bin/node
// Copy the bodies

const req = require('request');
const fs = require('fs');

req(process.argv[2], (err, res, body) => {
  if (err) throw err;
  fs.writeFile('loripsum', JSON.parse(body), 'utf-8', error => {
    if (error) throw error;
  });
});
