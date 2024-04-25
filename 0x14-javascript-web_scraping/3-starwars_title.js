#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

request
  .get(`https://swapi-api.alx-tools.com/api/films/${movieId}`)
  .on('response', function (response) {
    console.log(response.data.title);
  });
