#!/usr/bin/node
const argument = process.argv[2];
const parsedInt = parseInt(argument);

if (Number.isInteger(parsedInt)) {
  for (let i = 0; i < parsedInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
