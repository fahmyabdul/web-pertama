$(window).load(function() {
	$(".loader").fadeOut('slow');
});

$(document).ready(function () {
	$(".pesan").click(function() {
		$(this).fadeOut('slow');
	});
    $('[data-toggle="tooltip"]').tooltip(); 
});