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
  console.log(body);
  for (let i = 0; i < body.results[0].length; i++) {
    if (body.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/'))
        counter += 1;
  }
  console.log(counter);
});
