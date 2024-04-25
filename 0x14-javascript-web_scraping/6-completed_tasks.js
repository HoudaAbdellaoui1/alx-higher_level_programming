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
  Object.keys(completedTasksByUser).forEach(userId => {
    output += `'${userId}': ${completedTasksByUser[userId]},\n `;
  });
  output = output.slice(0, -2);
  output += ' }';
  console.log(output);
});
