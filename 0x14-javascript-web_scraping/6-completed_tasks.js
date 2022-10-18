#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const ans = {};

request(url, handle);

function handle (error, response, body) {
  if (error) {
    throw error;
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    for (let i = 0; i < data.length; i++) {
      if (data[i].completed) {
        if (ans[data[i].userId]) {
          ans[data[i].userId] += 1;
        } else {
          ans[data[i].userId] = 1;
        }
      }
    }
  }

  console.log(ans);
}
