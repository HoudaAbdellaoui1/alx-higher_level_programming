#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const urcl = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(body);
//   const movie = JSON.parse(body);
//   console.log(movie.title);
});
