$(document).ready(function(ev){

			if($(window).scrollTop() > 100)
				$(window).scrollTop($(window).scrollTop()+1);

	  smoothScroll.init();

			$(".navbar-toggle").click(function(ev){
				if($(this).hasClass("collapsed")){
					$('#header').addClass('scrolled');
				} else if($(window).scrollTop() < 100) {
					$('#header').removeClass('scrolled');
				}
			});

		$(window).scroll(function() {
			if ( $(window).scrollTop() >= 100 ) {
				$('#header').addClass('scrolled');
			} else {
				$('#header').removeClass('scrolled');
			}
		});
	})
