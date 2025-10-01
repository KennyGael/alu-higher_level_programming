#!/usr/bin/node
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  console.log('%s is %s', process.argv[2], process.argv[3]);
} else {
  console.log('%s is undefined', process.argv[2]);
}
