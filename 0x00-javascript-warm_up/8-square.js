#!/usr/bin/node
const numb = parseInt(process.argv[2]);
let i;

if (isNaN(numb)) {
  console.log('Missing size');
} else {
  for (i = 0; i < numb; i++) {
    console.log('X'.repeat(numb));
  }
}
