#!/usr/bin/node
const request = require('request');
const episodeURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(episodeURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(response.body);
  console.log(json.title);
});
