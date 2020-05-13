#!/usr/bin/node
// Star Wars title

const req = require('request');
const movieURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(movieURL, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
