document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
    $.get(url, function(data, textStatus) {
	$('#hello').text(data.hello);
    });
});
