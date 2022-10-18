#!/usr/bin/node

const request = require('request');

const episode = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episode}`;
request(url, (error, response, body) => {
  if (error) throw error;
  const obj = JSON.parse(body);
  console.log(obj.title);
});
