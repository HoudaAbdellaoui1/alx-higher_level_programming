#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasksByUser = todos.reduce((acc, todo) => {
    if (todo.completed) {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
    }
    return acc;
  }, {});

  let output = '{ ';
  const keys = Object.keys(completedTasksByUser);
  keys.forEach((userId, index) => {
    output += `'${userId}': ${completedTasksByUser[userId]}`;
    if (index !== keys.length - 1) {
      output += ',\n ';
    }
  });
  output += ' }';
  console.log(output);
});
