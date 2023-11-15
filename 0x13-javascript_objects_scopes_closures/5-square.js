#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

// A class square that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
