#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let z = 0; z < this.width; z++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
