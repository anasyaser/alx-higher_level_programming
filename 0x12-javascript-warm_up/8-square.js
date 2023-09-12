#!/usr/bin/node
const args = process.argv;
const size = Number(args[2]);
if (size) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
