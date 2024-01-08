#!/usr/bin/node

const argument = process.argv[2];
const parsed_int = parseInt(argument);

if (Number.isInteger(parsed_int)) {
  console.log('My number: ' + parsed_int);
} else {
  console.log('Not a number');
}
