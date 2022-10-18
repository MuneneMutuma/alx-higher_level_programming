#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
	let results = JSON.parse(body).results;
	let count = 0;
	const link = "https://swapi-api.hbtn.io/api/people/18/";

	for (let i = 0; i < results.length; i++) {
		let characters = results[i].characters;
		for (let x = 0; x < characters.length; x++) {
			if (characters[x] === link) count++;
		}
	}
	console.log(count);
})
