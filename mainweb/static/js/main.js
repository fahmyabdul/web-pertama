$(window).load(function() {
	$(".loader").fadeOut('slow');
});
$(document).ready(function () {
	$(".err").click(function() {
		$(this).fadeOut('slow');
	});
	$(document).on("scroll", onScroll);
		 
	$('a[href^="#"]').on('click', function (e) {
		e.preventDefault();
		$(document).off("scroll");
		 
		$('a').parent().each(function () {
			$(this).removeClass('active');
		});
		$(this).parent().addClass('active');
		 
		var target = this.hash;
		$target = $(target);
		$('html, body').stop().animate({
			'scrollTop': $target.offset().top+2
		}, 500, 'swing', function () {
			window.location.hash = target;
			$(document).on("scroll", onScroll);
		});
	});
});

function onScroll(event){
	var scrollPos = $(document).scrollTop();
	$('#navbar ul li').each(function () {
		var currLink = $(this);
		var refElement = $(currLink.children().attr("href"));
		if (refElement.position().top <= scrollPos -540 && refElement.position().top + refElement.height() > scrollPos -545) {
			$('#navbar ul li').removeClass("active");
			currLink.addClass("active");
		}else if (refElement.position().top <= scrollPos -400 && refElement.position().top + refElement.height() > scrollPos -400) {
			$('#navbar ul li').removeClass("active");
			currLink.addClass("active");
		}else if (refElement.position().top == 0){
			$('#navbar ul li').removeClass("active");
			$('[data-id=profil]').addClass("active");
		}else{
			currLink.removeClass("active");
		}
	});
}