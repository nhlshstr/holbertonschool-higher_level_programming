#!/usr/bin/node
// Gets status code

const req = require('request');

req(process.argv[2], (err, res, body) => {
  if (err) throw err;
  console.log('code: ' + res.statusCode);
});
