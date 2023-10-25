#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(response.body);
  const res = {};
  for (let i = 0; i < json.length; i++) {
    if (json[i].completed) {
      const userId = json[i].userId;
      if (!res[userId]) {
        res[userId] = 0;
      }
      res[userId]++;
    }
  }
  console.log(res);
});
