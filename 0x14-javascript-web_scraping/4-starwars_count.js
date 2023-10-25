#!/usr/bin/node
const request = require('request');
const episodesURL = process.argv[2];
request(episodesURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
    const json = JSON.parse(response.body);
    const results = json.results;
  let count = 0;
    for (let i = 0; i < results.length; i++) {
      let characters = results[i].characters
      for (let j = 0; j < characters.length; j++) {
	  if (characters[j].includes('/18/')) {
            count += 1;
	  }
    }
  }
  console.log(count);
});
