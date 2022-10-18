#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  const results = JSON.parse(body).results;
  let count = 0;
  if (error) {
    throw error;
  } else if (response.statusCode === 200) {
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let x = 0; x < characters.length; x++) {
        if (characters[x].includes('18')) count++;
      }
    }
    console.log(count);
  }
});
