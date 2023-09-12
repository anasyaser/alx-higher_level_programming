#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  if (a) {
    return a * factorial(a - 1);
  } else {
    return (1);
  }
}
console.log(factorial(Number(args[2])));
