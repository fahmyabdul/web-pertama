$(window).load(function() {
	$(".loader").fadeOut('slow');
});

$(document).ready(function () {
	$(".err").click(function() {
		$(this).fadeOut('slow');
	});
	$("body").css('overflow-y','auto');
});