#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
    const json = JSON.parse(response.body);
    let res = {'1': 0,
	       '2': 0,
	       '3': 0,
	       '4': 0,
	       '5': 0,
	       '6': 0,
	       '7': 0,
	       '8': 0,
	       '9': 0,
	       '10': 0};
    for (let i = 0; i < json.length; i++) {
	if (json[i].completed) {
	    let userId = json[i].userId;
            res[userId]++;
	}
    }
    console.log(res);
});
