#!/usr/bin/node
const Square = require('./5-Square');

class Square extends Square {
  constructor (l) {
    super(l, l);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
