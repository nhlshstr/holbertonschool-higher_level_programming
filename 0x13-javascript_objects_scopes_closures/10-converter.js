#!/usr/bin/node
// Base
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
