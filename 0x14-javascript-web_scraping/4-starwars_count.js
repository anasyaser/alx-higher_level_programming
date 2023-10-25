#!/usr/bin/node
const request = require('request');
const episodesURL = process.argv[2];
const charURL = 'https://swapi-api.alx-tools.com/api/people/18/';
request(episodesURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(response.body);
  let count = 0;
  for (let i = 0; i < json.results.length; i++) {
    if (json.results[i].characters.includes(charURL)) {
      count += 1;
    }
  }
  console.log(count);
});
