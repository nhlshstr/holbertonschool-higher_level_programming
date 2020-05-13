#!/usr/bin/node
// Number of movies where the character
// “Wedge Antilles” is present.

const req = require('request');
const endpoint = process.argv[2];
req(endpoint, (err, res, body) => {
  if (err) throw err;
  const movies = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < movies.count; i++) {
    if (movies.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count += 1;
    }
  }
  console.log(count);
});
