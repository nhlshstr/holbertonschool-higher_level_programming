#!/usr/bin/node
// returns the reversed version of a list

exports.esrever = function (list) {
  const listRev = [];
  for (let i = 0; i < list.length; i++) {
    listRev[i] = list[list.length - 1 - i];
  }
  return listRev;
};
