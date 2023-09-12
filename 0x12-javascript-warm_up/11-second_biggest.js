#!/usr/bin/node
const args = process.argv;
const sliced = args.slice(2).map(Number);
function getMax (arr) {
  let mx = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > mx) {
      mx = arr[i];
    }
  }
  return mx;
}
if (args[2] && args.length > 3) {
  const maxNum = getMax(sliced);
  let curr = sliced[0];
  for (let i = 0; i < sliced.length; i++) {
    if (sliced[i] > curr && sliced[i] < maxNum) {
      curr = sliced[i];
    }
  }
  console.log(curr);
} else {
  console.log(0);
}
