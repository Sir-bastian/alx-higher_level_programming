#!/usr/bin/node

const argument = process.argv[2];
const parsedInt = parseInt(argument);
const character = 'X';
const result = character.repeat(parsedInt);

if (Number.isInteger(parsedInt)) {
  for (let i = 0; i < parsedInt; i++) {
    console.log(result);
  }
} else {
  console.log('Missing size');
}
