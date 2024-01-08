#!/usr/bin/node

let argument = process.argv[2];

if (argument === undefined) {
	console.log('No aargument');
} else {
	console.log(argument);
}
