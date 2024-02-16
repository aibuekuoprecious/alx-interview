#!/usr/bin/node

const request = require('request');

const getFilmCharacters = async (filmId) => {
  try {
    const filmResponse = await requestPromise(
      'https://swapi-api.hbtn.io/api/films/' + filmId
    );
    const filmData = JSON.parse(filmResponse);
    const characters = filmData.characters;
    await printCharactersInExactOrder(characters, 0);
  } catch (error) {
    throw error;
  }
};

const printCharactersInExactOrder = async (characters, index) => {
  if (index === characters.length) return;
  try {
    const characterResponse = await requestPromise(characters[index]);
    const characterData = JSON.parse(characterResponse);
    console.log(characterData.name);
    await printCharactersInExactOrder(characters, index + 1);
  } catch (error) {
    throw error;
  }
};

const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
};

getFilmCharacters(process.argv[2]);
