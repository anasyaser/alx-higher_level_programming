#!/usr/bin/node
const request = require('request');
const episodesURL = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(episodesURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(response.body);
  const characters = json.characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      const jsonInner = JSON.parse(response.body);
      console.log(jsonInner.name);
    });
  }
});
