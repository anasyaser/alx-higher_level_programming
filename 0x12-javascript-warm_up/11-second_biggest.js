#!/usr/bin/node
const args = process.argv;
const sliced = args.slice(2).map(Number).sort((a, b) => b - a);
if (args[2] && args.length > 3) {
  console.log(sliced[1]);
} else {
  console.log(0);
}
