#!/usr/bin/node
exports.esrever = function (list) {
  const lst = [];
  for (let i = list.length; i > 0; i--) {
    lst.push(list[i - 1]);
  }
  return lst;
};
