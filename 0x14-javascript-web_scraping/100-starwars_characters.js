#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const getMovieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
// Get the movie
request(getMovieUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const characterUrl of characters) {
    request(characterUrl, (err, res, body) => {
      if (err) { console.error(err); return; }
      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  }
});
