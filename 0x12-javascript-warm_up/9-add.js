#!/usr/bin/node
const args = process.argv;
function add (a, b) {
  console.log(Number(a) + Number(b));
}
add(args[2], args[3]);
