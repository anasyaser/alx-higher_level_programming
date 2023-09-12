#!/usr/bin/node
const args = process.argv;
const num = Number(args[2]);
if (num) {
  console.log(num);
} else {
  console.log('Not a number');
}
