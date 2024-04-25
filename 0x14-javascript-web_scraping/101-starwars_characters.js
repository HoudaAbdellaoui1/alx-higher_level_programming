#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const getMovieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
// Get the movie
request(getMovieUrl, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    returnCharactersByOrder(characters, 0);
  }
});

function returnCharactersByOrder (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        returnCharactersByOrder(characters, index + 1);
      }
    }
  });
}
