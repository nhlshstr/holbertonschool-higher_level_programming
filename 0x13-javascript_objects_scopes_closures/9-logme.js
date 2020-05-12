#!/usr/bin/node
// prints the number of arguments
// already printed and the new argument
exports.logMe = function (item) {
  this.i = this.i || 0;
  console.log(this.i + ': ' + item);
  this.i++;
};
