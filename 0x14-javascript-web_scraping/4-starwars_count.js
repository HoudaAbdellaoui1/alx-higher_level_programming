#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const urcl = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let counter = 0;
  for (let i = 0; i < body.results.length; i++) {
    if (data.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) { counter += 1; }
  }
  console.log(counter);
});
