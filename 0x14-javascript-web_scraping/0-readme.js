#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const fileContent = fs.readFileSync(filePath, 'utf8');
console.log(fileContent);
