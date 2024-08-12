#!/usr/bin/env node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
	console.error("Please provide a Movie ID as a positional argument.");
	process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
	if (error) {
		console.error("An error occurred:", error);
		return;
	}

	const filmData = JSON.parse(body);

	const characterUrls = filmData.characters;

	characterUrls.forEach((url) => {
		request(url, (error, response, body) => {
		if (error) {
			console.error("An error occurred:", error);
			return;
		}

		const characterData = JSON.parse(body);
		console.log(characterData.name);
		});
	});
});
