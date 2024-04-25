#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.appendFile(filePath, stringToWrite, function (err) {
  if (err) throw err;
});
