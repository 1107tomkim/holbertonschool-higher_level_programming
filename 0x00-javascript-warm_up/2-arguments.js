#!/usr/bin/node
const string1 = 'No argument';
const string2 = 'Argument found';
const string3 = 'Arguments found';

if (process.argv.length = 1) {
	console.log(string1);
} else if (process.argv.length === 3) {
	console.log(string2);
} else {
	console.log(string3);
}
