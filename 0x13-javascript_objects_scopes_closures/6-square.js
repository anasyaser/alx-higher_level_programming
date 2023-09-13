#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (l) {
    super(l, l);
  }

  charPrint (c) {
    let chr = 'X';
    if (c) {
      chr = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }
}
module.exports = Square;
