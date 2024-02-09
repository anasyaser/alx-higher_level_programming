const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function(data, textStatus)
      {
	  $.each(data.results, function(index, film)
		 {
		     $('#list_movies').append($('<li></li>').text(film.title));
		 });
      });
