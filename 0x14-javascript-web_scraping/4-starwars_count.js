#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let counter = 0;
  const films = JSON.parse(body).results;
  films.forEach(film => {
    if (film.characters.includes(
      'https://swapi-api.alx-tools.com/api/people/18/')) {
      counter++;
    }
  });

  console.log(counter);
});
