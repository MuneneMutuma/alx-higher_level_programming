$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (films, status) {
  $.each(films.results, function (i, film) {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  });
});
