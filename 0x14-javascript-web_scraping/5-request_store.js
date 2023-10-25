#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(filePath, body, function (err) {
    if (err) {
      console.log(err);
    }
  });
});
