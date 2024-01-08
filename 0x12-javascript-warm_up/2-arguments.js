#!/usr/bin/node

const args = process.argv.length - 2;
if (args === 0) {i
	console.log('No argument');
}
else if (args === 1) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
